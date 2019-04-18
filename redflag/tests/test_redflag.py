from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class RedflagTests(APITestCase):
    redflag_url = '/api/v1/redflags/'
    login_url = '/api/v1/accounts/login/'
    register_url = '/api/v1/accounts/signup/'

    def setUp(self):
        user_data = {
            "username": "jane",
            "email": "jane@bg.com",
            "password": "simplepassword"
        }

        self.client.post(self.register_url, user_data, format='json')
        login_credentials = {'username': 'jane', 'password': 'simplepassword'}
        login_response = self.client.post(
            self.login_url, login_credentials, format='json')

        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.test_token = login_response.data.get("token")
        self.auth_header = 'Bearer {}'.format(self.test_token)

    def test_create_redflag(self):
        """test successful creation of a redflag"""
        post_data={
            "title": "test one",
            "comment": "this is the first comment",
            "image": "imageone",
            "video": "videoone",
            "location": "19, 24"
        }
        client=APIClient(enforce_csrf_checks=True)
        response=client.post(self.redflag_url, post_data,
                               HTTP_AUTHORIZATION=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_redflag_failed(self):
        """test unsuccessful creation of a redflag"""
        post_data={
            "comment": "this is the first comment",
            "image": "imageone",
            "video": "videoone",
            "location": "19, 24"
        }
        client=APIClient(enforce_csrf_checks=True)
        response=client.post(self.redflag_url, post_data,
                               HTTP_AUTHORIZATION=self.auth_header, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

