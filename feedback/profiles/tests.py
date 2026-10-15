from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from PIL import Image

from .models import UserProfile


class ProfileViewsTests(TestCase):
    def setUp(self):
        self.media_directory = TemporaryDirectory()
        self.addCleanup(self.media_directory.cleanup)
        self.settings_override = override_settings(
            MEDIA_ROOT=Path(self.media_directory.name),
            DEBUG=True,
        )
        self.settings_override.enable()
        self.addCleanup(self.settings_override.disable)

    def make_image_upload(self, name="picture.png"):
        image_data = BytesIO()
        Image.new("RGB", (1, 1), color="purple").save(image_data, format="PNG")
        return SimpleUploadedFile(
            name,
            image_data.getvalue(),
            content_type="image/png",
        )

    def test_homepage_renders_profile_upload_form(self):
        response = self.client.get(reverse("profiles:home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/create_profile.html")
        self.assertContains(response, 'name="image"')
        self.assertContains(response, 'enctype="multipart/form-data"')
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_valid_image_upload_is_saved_and_listed(self):
        response = self.client.post(
            reverse("profiles:create-profile"),
            {"image": self.make_image_upload()},
        )

        self.assertRedirects(response, reverse("profiles:profile-list"))
        profile = UserProfile.objects.get()
        self.assertEqual(profile.image.name, "images/picture.png")
        self.assertTrue(
            (Path(self.media_directory.name) / profile.image.name).is_file()
        )

        response = self.client.get(reverse("profiles:profile-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/user_profile.html")
        self.assertContains(response, 'src="/user-media/images/picture.png"')

    def test_profile_list_displays_uploaded_images(self):
        profile = UserProfile()
        profile.image.save(
            "existing.png",
            self.make_image_upload("existing.png"),
        )

        response = self.client.get("/profiles/lists")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/user_profile.html")
        self.assertContains(response, f'src="{profile.image.url}"')
        self.assertContains(response, 'alt="Uploaded profile image"')

    def test_pdf_upload_is_rejected(self):
        response = self.client.post(
            reverse("profiles:create-profile"),
            {
                "image": SimpleUploadedFile(
                    "document.pdf",
                    b"%PDF-1.4 this is not an image",
                    content_type="application/pdf",
                )
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Upload a valid image")
        self.assertEqual(UserProfile.objects.count(), 0)
