from django.test import TestCase

from django.contrib.auth.models import User


class AdminModelTests(TestCase):

    def test_django_admin_login(self):
        admin_user = User.objects.create(
            username = "admin",
            password = "Password123",
            is_superuser = True,
            is_staff = True
        )

        self.assertEqual(admin_user.username,"admin")
        self.assertIsInstance(admin_user,User)



