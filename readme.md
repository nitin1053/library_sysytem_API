



Personal Library System API

This is a RESTful API for managing a personal library system. It allows users to add books to their personal library, update book details, delete books, and list the books they have added.

python manage.py runserver




Personal Library System API
This is a RESTful API for managing a personal library system. It allows users to add books to their personal library, update book details, delete books, and list the books they have added.

Setup Instructions
Clone the repository:


Install dependencies:


python manage.py runserver
Access the API at http://localhost:8000/.

API Endpoint Documentation
User Registration
URL: /register/

Method: POST

Description: Register a new user.

Request Body:
{
    "email": "example@example.com",
    "password": "your_password",
    "username": "example_user"
}


User Sign-In
URL: /signin/

Method: POST

Description: Sign in an existing user.

Request Body:
{
    "email": "example@example.com",
    "password": "your_password"
}


List Books
URL: /api/books/

Method: GET

Description: Retrieve a list of all books in the library.

Add Book
URL: /api/books/

Method: POST

Description: Add a new book to the library.

Request Body:
{
    "title": "Book Title",
    "authors": "Author Name",
    "isbn": "1234567890123"
}


Book Details
URL: /api/books/<isbn>/

Method: GET

Description: Retrieve the details of a book identified by its ISBN.

Update Book
URL: /api/books/<isbn>/

Method: PUT

Description: Update the details of a specific book identified by its ISBN.

Request Body: (Provide all fields for a complete update)

Delete Book
URL: /api/books/<isbn>/

Method: DELETE

Description: Delete a specific book from the library.

Authentication
Authentication is required for some endpoints. The API uses JWT token-based authentication. After successful registration or sign-in, the API will return an access token which should be included in the Authorization header for authenticated requests.
