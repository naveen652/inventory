from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class ItemViewSet(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="postgres", password="naveen")

    def test_obtain_token(self):
        url = reverse('token_obtain_pair')
        data = {
            "username": "postgres",
            "password": "naveen"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_refresh_token(self):
        # First obtain a token
        url = reverse('token_obtain_pair')
        data = {
            "username": "postgres",
            "password": "naveen"
        }
        response = self.client.post(url, data, format='json')
        refresh_token = response.data['refresh']

        # Now refresh the token
        url = reverse('token_refresh')
        data = {"refresh": refresh_token}
        refresh_response = self.client.post(url, data, format='json')
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn("access", refresh_response.data)

    def test_protected_view(self):
        # Obtain a token first
        url = reverse('token_obtain_pair')
        data = {
            "username": "postgres",
            "password": "naveen"
        }
        response = self.client.post(url, data, format='json')
        access_token = response.data['access']

        # Access a protected view
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        url = reverse('protected_view')  # Adjust to your view's URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "You are authenticated"})
