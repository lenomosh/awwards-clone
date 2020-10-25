from django.contrib.auth.models import User
from django.test import TestCase


class TestUser(TestCase):

    def setUp(self) -> None:
        self.user = User(
            username="test_user",
            password="password",
            email="test@gmail.com",
            first_name="John",
            last_name="Doe")

    def test_instance_of_user(self):
        self.user.save()
        query = User.objects.all()

        self.assertIsInstance(query[0], User)

    def test_create_user(self):
        self.user.save()
        query = User.objects.all()
        self.assertEqual(len(query) , 1)

    def test_delete_user(self):
        self.user.save()
        query = User.objects.all()
        self.assertEqual(len(query), 1)
        self.user.delete()
        query = User.objects.all()
        self.assertEqual(len(query), 0)

    def test_update_user(self):
        self.user.save()
        self.user.username = "Lennox"
        self.user.save()
        self.assertEqual(self.user.username, "Lennox")
