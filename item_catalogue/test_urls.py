# A file to test the urls of the item catalogue
# 3rd Party Imports
from django.test import SimpleTestCase
from django.urls import reverse, resolve
# Internal
from item_catalogue.views import catalogue_menu


class TestMenuUrls(SimpleTestCase):
    """
    This class is to test the catalogue
    menu url
    """
    def test_catalogue_menu_resolved(self):
        url = reverse('catalouge_menu')
        self.assertEquals(resolve(url).func, catalogue_menu)
