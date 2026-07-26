from django.test import TestCase

from .models import UserName


class HomePageTests(TestCase):
    def test_page_opens(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_name_is_saved(self):
        response = self.client.post("/", {"name": "Анна"})
        self.assertContains(response, "Привет, Анна!")
        self.assertTrue(UserName.objects.filter(name="Анна").exists())

    def test_empty_name_shows_error(self):
        response = self.client.post("/", {"name": "   "})
        self.assertContains(response, "Введите имя")
        self.assertEqual(UserName.objects.count(), 0)
