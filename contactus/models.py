# 3rd Party Imports
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    A class for the contact us
    model
    """
    message_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contact_user", null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, default="")
    phone = PhoneNumberField(null=True)
    message = models.TextField()

    class Meta:
        """
        A class for keep dates
        chronological
        """
        ordering = ['created_date']

    def __str__(self):
        return self.name
