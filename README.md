# Book Store

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python" alt="Python 3.12+" />
  <img src="https://img.shields.io/badge/Django-6.1.1-092E20?style=for-the-badge&logo=django" alt="Django 6.1.1" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite" alt="SQLite" />
</p>

A small Django application for managing and displaying a collection of books. This project demonstrates a simple bookstore app with a list view, detail view, slug-based URLs, and a basic test suite.

## Features

- Browse all books on the home page
- Open a dedicated detail page for each book
- Show title, author, rating, and bestseller status
- Use clean slug URLs such as `/the-hobbit`
- Include a regression test for the detail view

## Demo

### Book list

![Book list page](docs/screenshots/book-list.svg)

### Book detail

![Book detail page](docs/screenshots/book-detail.svg)

## Tech Stack

- Python 3.12+
- Django 6.1.1
- SQLite

## Project Structure

```text
book_store/
├── .gitignore
├── LICENSE
├── README.md
├── bookstore/
│   ├── manage.py
│   ├── bookstore/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── book_outlet/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations/
│       ├── models.py
│       ├── templates/
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── docs/
│   └── screenshots/
│       ├── book-list.svg
│       └── book-detail.svg
├── db.sqlite3
└── venv/
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/dalteg/bookstore.git
cd bookstore
```

2. Create and activate a virtual environment:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. Install Django:

```bash
pip install django
```

4. Apply database migrations:

```bash
cd bookstore
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open the app:

```text
http://127.0.0.1:8000/
```

## Running Tests

```bash
cd bookstore
python manage.py test book_outlet
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome. If you want to improve the app or add features, open a pull request with a clear description of the change.
