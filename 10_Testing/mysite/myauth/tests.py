from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class GetCookieViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test_user", password="qwerty", is_superuser=True)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_get_cookie_view(self):
        response = self.client.get(reverse("myauth:cookie-get"))
        self.assertContains(response, "Cookie value")


class FooBarViewTest(TestCase):
    def test_foo_bar_view(self):
        response = self.client.get(reverse("myauth:foo-bar"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.headers['content-type'], 'application/json',
        )
        expected_data = {"foo": "bar", "spam": "eggs"}
        self.assertJSONEqual(response.content, expected_data)
