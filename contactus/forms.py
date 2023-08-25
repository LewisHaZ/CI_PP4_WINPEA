# 3rd Party Imports
from django import forms
from crispy_forms.helper import FormHelper
from phonenumber_field.formfields import PhoneNumberField

# Internal
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A class to initialise the content
    for the contact form
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+447123456789')}
    ))

    class Meta:
        model = Contact
        fields = (
            'name',
            'phone',
            'email',
            'message'
        )