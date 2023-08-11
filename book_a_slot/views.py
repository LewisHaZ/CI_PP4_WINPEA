# Imports
# 3rd Party
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views import generic
from django.contrib.auth.models import User

# Internal
from .models import Slot, Booking
from .forms import BookingForm


def get_user_instance(request, User):
    """
    Picks up user details when they
    are logged into the system
    """
    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()

    return user


class Reservations(View):
    """
    User view for making bookings
    If user is already logged in then email is
    set to a booking email
    """
    template_name = 'book_a_slot/visit_store.html'

    def get(self, request, *args, **kwargs):
        """
        Gets user email and place into the input
        """
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})

        else:
            booking_form = BookingForm()

        return render(request, 'book_a_slot/visit_store.html',
                      {'booking_form': booking_form})

    def post(self, request):

        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect(Confirmed())
        else:
            booking_form = BookingForm()

        return render(request, 'book_a_slot/slot_confirmed.html')


class Confirmed(generic.DetailView):
    """
    Loads a confirmation page
    """
    template_name = 'book_a_slot/slot_confirmed.html'

    def get(self, request):
        return render(request, 'book_a_slot/slot_confirmed.html')
