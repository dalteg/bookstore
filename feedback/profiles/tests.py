from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings


class ProfileUploadPageTests(TestCase):
    def test_homepage_renders_profile_upload_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/create_profile.html")
        self.assertContains(response, 'name="user_image"')
        self.assertContains(response, "Upload!")

    def test_rendered_csrf_token_is_accepted_on_upload_post(self):
        client = Client(enforce_csrf_checks=True)
        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="csrfmiddlewaretoken"')
        csrf_token = response.cookies["csrftoken"].value

        missing_token_response = client.post("/profiles", {})
        self.assertEqual(missing_token_response.status_code, 403)

        tokenized_response = client.post(
            "/profiles",
            {},
            HTTP_X_CSRFTOKEN=csrf_token,
        )
        self.assertEqual(tokenized_response.status_code, 400)
        self.assertContains(
            tokenized_response,
            "This field is required.",
            status_code=400,
        )

    def test_upload_saves_file_under_configured_media_root(self):
        with TemporaryDirectory() as temp_directory:
            with override_settings(MEDIA_ROOT=Path(temp_directory)):
                response = self.client.post(
                    "/profiles/",
                    {
                        "user_image": SimpleUploadedFile(
                            "picture.png",
                            b"test image data",
                            content_type="image/png",
                        )
                    },
                )

                self.assertRedirects(
                    response,
                    "/",
                    fetch_redirect_response=False,
                )
                self.assertEqual(
                    (Path(temp_directory) / "picture.png").read_bytes(),
                    b"test image data",
                )

    def test_upload_without_file_returns_clear_error(self):
        response = self.client.post("/profiles", {})

        self.assertEqual(response.status_code, 400)
        self.assertContains(
            response,
            "This field is required.",
            status_code=400,
        )