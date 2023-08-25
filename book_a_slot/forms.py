# 3rd Party Imports
from django import forms
from crispy_forms.helper import FormHelper
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
# Internal
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    A class to initialise the content
    for the booking form
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    requested_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+447123456789')}))

    class Meta:
        """
        A class to set up the
        various fields of the
        booking app
        """
        model = Booking
        fields = (
            'name',
            'phone',
            'email',
            'guest_count',
            'requested_date',
            'requested_time',
            'slot'
        )
