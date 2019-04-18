from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase


class TestSignup(APITestCase):
    def test_signup_with_wrong_email(self):
        """
        Ensure we cannot signup with wrong email.
        """
        data = {"username": "bison",
                "password": "12345",
                "email": "biso.com"
                }
        url = reverse("signup")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_signup_user_with_valid_data(self):
        """
        Ensure user can sign up with valid data.
        """
        data = {"username": "bisonlou",
                "password": "Pa$$word123",
                "email": "bisonlou@gmail.com"
                }
        url = reverse("signup")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_signup_duplicate_user_with_valid_data(self):
        """
        Ensure user can sign up with valid data.
        """
        self.superuser = User.objects.create_superuser(
            "user1", "bisonlou@gmail.com", "Pa$$word123"
        )
        data = {"username": "user1",
                "password": "Pa$$word123",
                "email": "bisonlou@gmail.com"
                }
        url = reverse("signup")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_signup_user_with_short_password(self):
        """
        Ensure user cannot signup with a password shorter than 8 chars.
        """
        data = {"username": "bisonlou",
                "password": "123",
                "email": "bisonlou@gmail.com"
                }
        url = reverse("signup")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_signup_user_with_guessable_password(self):
        """
        Ensure user cannot signup with a password
        similar to his username or among common passwords.
        """
        data = {"username": "bisonlou",
                "password": 'bison',
                "email": "bisonlou@gmail.com"
                }
        url = reverse("signup")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 400)

