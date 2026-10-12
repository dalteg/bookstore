from django.test import TestCase
from .models import Review


class ReviewListViewTests(TestCase):
    def test_list_shows_only_reviews_rated_above_four(self):
        Review.objects.create(
            user_name="High rating",
            review_text="Good",
            rating=5,
        )
        Review.objects.create(
            user_name="Lower rating",
            review_text="Okay",
            rating=4,
        )

        response = self.client.get("/reviews")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "High rating")
        self.assertNotContains(response, "Lower rating")

    def test_homepage_still_displays_review_form(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="user_name"')

    def test_submitting_review_saves_it_and_redirects(self):
        response = self.client.post(
            "/",
            {
                "user_name": "New reviewer",
                "review_text": "Helpful feedback",
                "rating": 5,
            },
        )

        self.assertRedirects(response, "/thank_you/")
        self.assertTrue(
            Review.objects.filter(
                user_name="New reviewer",
                review_text="Helpful feedback",
                rating=5,
            ).exists()
        )
