from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


class SnacksTests(TestCase):
    def setUp(self):
        """
        create a mock database to run the test on it
        """
        purchaser = get_user_model().objects.create(
            username="tester", password="tester"
        )
        Snack.objects.create(name="test_name", purchaser=purchaser)

    def test_list_page_status_code(self):
        """
        test the status_code of list page
        """
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        """
        test the used template for the list page
        """
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_list_page_context(self):
        """
        test the records in the database
        """
        url = reverse("snack_list")
        response = self.client.get(url)
        snack = response.context["object_list"]
        self.assertEqual(len(snack), 1)
        self.assertEqual(snack[0].name, "test_name")
        self.assertEqual(snack[0].description, '')
        self.assertEqual(snack[0].purchaser.username, "tester")

    def test_detail_page_status_code(self):
        """
        test the status_code of detail page
        """
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        """
        test the used template of detail page
        """
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertTemplateUsed(response, "base.html")

    def test_detail_page_context(self):
        """
        test the records in the database
        :return:
        """
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        snack = response.context["snack"]
        self.assertEqual(snack.name, "test_name")
        self.assertEqual(snack.description, '')
        self.assertEqual(snack.purchaser.username, "tester")