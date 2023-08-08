# Imports
# 3rd Party
from django.contrib import admin
# Internal
from .models import Slot, Guest, Booking


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot_id', 'slot_name', 'max_slots')


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_id', 'name', 'email', 'phone')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = (
        'guest_count',
        'status',
        'slot_id',
        'requested_date',
        'requested_time'
        )
    list_display = ('booking_id', 'guest', 'guest_count', 'status',
                    'slot', 'requested_date', 'requested_time')
