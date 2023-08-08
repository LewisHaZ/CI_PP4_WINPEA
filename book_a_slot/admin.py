# Imports
# 3rd Party
from django.contrib import admin
# Internal
from .models import Slot, User, Booking


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot_id', 'slot_name', 'max_slots')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'email', 'phone')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('people_count', 'status', 'slot_id')
    list_display = ('booking_id', 'user', 'people_count', 'status',
                    'slot', 'requested_date', 'requested_time')
