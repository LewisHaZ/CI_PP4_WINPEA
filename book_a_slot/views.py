# Imports
# 3rd Party
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView

# Internal
from .models import Slot, Booking
from .forms import BookingForm


def get_user_instance(request):
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
            return render(request, 'book_a_slot/slot_confirmed.html')
        else:
            booking_form = BookingForm()

        return render(request, 'book_a_slot/visit_store.html', {'booking_form': booking_form})


class Confirmed(generic.DetailView):
    """
    Loads a confirmation page
    """
    template_name = 'book_a_slot/slot_confirmed.html'

    def get(self, request):
        return render(request, 'book_a_slot/visit_store.html')


class BookingList(generic.DetailView):
    """
    Displays bookings to the user
    that they have made
    """
    template_name = 'booking_list.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)

            return render(
                request, 'book_a_slot/booking_list.html', {
                    'bookings': bookings})
        else:
            return redirect('accounts/login.html')


class EditBooking(SuccessMessageMixin, UpdateView):
    """
    Allow users that are logged in/registered
    to edit their bookings
    """
    model = Booking
    form_class = BookingForm
    template_name = 'book_a_slot/edit_booking.html'
    success_message = 'Booking was updated.'

    def get_success_url(self, **kwargs):
        return reverse('booking_list')
