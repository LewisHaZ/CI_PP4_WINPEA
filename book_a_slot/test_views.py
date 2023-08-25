# A file to test the views of the book a slot app
# 3rd Party Imports
from django.test import TestCase, Client
from django.urls import reverse


class TestBookingsViews(TestCase):
    """
    This is a class to test
    the views.py of the book a slot app
    """
    def setUp(self):
        self.client = Client()
        self.reservations_url = reverse('reservations')
        self.confirmed_url = reverse('confirmed')
        self.edit_booking_url = reverse('booking_list')

    def test_reservations_GET(self):
        response = self.client.get(self.reservations_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_a_slot/visit_store.html')

    def test_confirmed_GET(self):
        response = self.client.get(self.confirmed_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_a_slot/visit_store.html')
