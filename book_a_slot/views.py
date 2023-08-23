# Imports
# 3rd Party
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator

# Internal
from .models import Booking
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
    success_message = 'Booking has been made successfully.'

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
            messages.success(
                request, "Booking successful, awaiting confirmation")
            return render(request, 'book_a_slot/slot_confirmed.html')

        return render(
            request,
            'book_a_slot/visit_store.html', {'booking_form': booking_form})


class Confirmed(generic.DetailView):
    """
    Loads a confirmation page
    """
    template_name = 'book_a_slot/slot_confirmed.html'

    def get(self, request):
        return render(request, 'book_a_slot/visit_store.html')


class BookingList(generic.ListView):
    """
    Displays bookings to the user
    that they have made
    """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'booking_list.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):

        booking = Booking.objects.all()
        paginator = Paginator(Booking.objects.all(), 4)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)

        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)

            return render(
                request, 'book_a_slot/booking_list.html', {
                    'booking': booking,
                    'bookings': bookings,
                    'booking_page': booking_page})
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


def cancel_booking(request, pk):
    """
    Delete the booking after it's been
    booked by a user with a Primary Key
    """
    booking = Booking.objects.get(pk=pk)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking successfully cancelled")
        return redirect('booking_list')

    return render(
        request, 'book_a_slot/cancel_booking.html', {'booking': booking})
