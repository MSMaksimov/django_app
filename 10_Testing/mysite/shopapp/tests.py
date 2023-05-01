from random import choices
from string import ascii_letters

from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from .models import Product
from .utils import add_two_numbers


class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 5)


class ProductCreateViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        permission_view = Permission.objects.get(codename="add_product")
        cls.user = User.objects.create_user(username="test_user", password="qwerty")
        cls.user.user_permissions.add(permission_view)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()
        self.client.force_login(self.user)

    def test_create_product(self):
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": self.product_name,
                "price": "123.45",
                "description": "A good table",
                "discount": "10",
            },
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )

