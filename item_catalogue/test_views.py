# A file to tests the views of the item catalogue
# 3rd Party Imports
from django.test import TestCase, Client
from django.urls import reverse


class TestCatalogueViews(TestCase):
    """
    A class to test
    the views.py of the catalogue app
    """
    def setUp(self):
        self.client = Client()
        self.catalogue_url = reverse('catalogue')

    def test_catalogue_GET(self):
        response = self.client.get(self.catalogue_url)

        self.assertEqual(response.status_code, 200)
