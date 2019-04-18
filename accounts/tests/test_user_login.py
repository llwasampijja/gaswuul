from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase


class TestLogin(APITestCase):
    def test_login_successful(self):
        self.create_user()
        data = {"username": "zack_atama", "password": "comebiteme"}
        response = self.login(data)
        self.assertEqual(response.status_code, 200)

    def test_login_password_missing(self):
        self.create_user()
        data = {"username": "zack_atama", "password": ""}
        response = self.login(data)
        self.assertEqual(response.status_code, 400)

    def test_login_wrong_password(self):
        self.create_user()
        data = {"username": "zack_atama", "password": "12345"}
        response = self.login(data)
        self.assertEqual(response.status_code, 400)

    def test_login_wrong_username(self):
        self.create_user()
        data = {"username": "zeus", "password": "Pa$$word123"}
        response = self.login(data)
        self.assertEqual(response.status_code, 400)

    def create_user(self):
        self.superuser = User.objects.create_superuser(
            "zack_atama", "zack.atama@andela.com", "comebiteme"
        )

    def login(self, kwags):
        self.username = kwags.get("username")
        self.password = kwags.get("password")

        url = reverse("login")
        data = {"username": self.username, "password": self.password}
        return self.client.post(url, data, format="json")
