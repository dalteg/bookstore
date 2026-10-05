from django.test import TestCase
from .models import Author, Book


class BookDetailViewTests(TestCase):
    def test_detail_page_displays_selected_book(self):
        author = Author.objects.create(
            first_name="J.R.R.",
            last_name="Tolkien",
        )
        book = Book.objects.create(
            title="The Hobbit",
            author=author,
            rating=5,
            is_bestselling=True,
        )

        response = self.client.get(f"/{book.slug}")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Hobbit")
        self.assertContains(response, "J.R.R. Tolkien")
