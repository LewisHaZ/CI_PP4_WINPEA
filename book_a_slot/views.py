# Imports
# 3rd Party
from django.shortcuts import render
from django.views import generic

# Internal
from .models import Slot, Guest, Booking

def visit_store(request):
    """
    a view to display the booking list
    for visiting the store
    """
    book_a_slot_list = Booking.objects.all()
    return render (
        request, 'book_a_slot/visit_store.html', {'book_a_slot_list': book_a_slot_list})
