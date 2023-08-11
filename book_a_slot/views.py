# Imports
# 3rd Party
from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User

# Internal
from .models import Slot, Guest, Booking
from .forms import BookingForm, GuestForm


class Reservations(View):
    """
    Guest view for making bookings
    """
    def get(self, request, *args, **kwargs):
        
        template_name = 'book_a_slot/visit_store.html'

        return render(
            request, "book_a_slot/visit_store.html",
            {'guest_form': GuestForm(), 'booking_form': BookingForm()})
    
    def post(self, request, User=user, *args, **kwargs):
        
        guest_form = GuestForm(data=request.POST)
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid() and guest_form.is_valid():
            guest_requested_date = request.POST.get('requested_date')
            guest_requested_time = request.POST.get('requested_time')
            guest_count = request.POST.get('guest_count')
        else:
            booking_form = BookingForm
        
        return render(request, "book_a_slot/visit_store.html",
                {'guest_form': guest_form,
                'booking_form': booking_form})