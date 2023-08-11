# Imports
# 3rd Party
from django.contrib import admin
from rangefilter.filters import DateRangeFilter
# Internal
from .models import Slot, Booking


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot_id', 'slot_name', 'max_slots')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
        'guest_count',
        'status',
        'slot_id',
        'requested_date',
        'requested_time',
        'created_date')
    list_display = (
        'booking_id',
        'user',
        'name',
        'phone',
        'guest_count',
        'status',
        'slot',
        'requested_date',
        'requested_time',
        'created_date')

    search_fields = ['guest__name']
    list_filter = (('requested_date', DateRangeFilter),)
