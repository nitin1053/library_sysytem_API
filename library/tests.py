from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Create some test books
        Book.objects.create(title='Book 1', authors='Author 1', isbn='1234567890123')
        Book.objects.create(title='Book 2', authors='Author 2', isbn='1234567890456')

    def test_register_user(self):
        url = reverse('register')
        data = {'email': 'newuser@example.com', 'password': 'newpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_sign_in(self):
        url = reverse('signin')
        data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_update_book(self):
        book = Book.objects.first()
        url = reverse('book-detail', args=[book.isbn])
        data = {'title': 'Updated Title', 'authors': 'Updated Author', 'publication_date': '2022-01-01', 'description': 'Updated Description'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_book(self):
        url = reverse('book-list-create')
        data = {'title': 'New Book', 'authors': 'New Author', 'isbn': '1234567890789'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_detail(self):
        book = Book.objects.first()
        url = reverse('book-detail', args=[book.isbn])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        book = Book.objects.first()
        url = reverse('book-detail', args=[book.isbn])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_books(self):
        url = reverse('book-list-create')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)