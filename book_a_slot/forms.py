# Imports
# 3rd Party
from django import forms
from crispy_forms.helper import FormHelper
from datetime import datetime


# Internal
from .models import Booking


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    requested_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    class Meta:
        model = Booking
        fields = (
            'name',
            'phone',
            'email',
            'guest_count',
            'requested_date',
            'requested_time'
        )
