# 3rd Party Imports
from django.contrib import admin
from rangefilter.filters import DateRangeFilter

# Internal
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    A class for the contact admin
    and the fields it needs to control
    """
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
        'created_date'
    )
    list_display = (
        'message_id',
        'user',
        'name',
        'message',
        'phone',
        'created_date'
    )

    search_fields = ['name']
    list_filter = (('created_date', DateRangeFilter),)
