# 3rd Party Imports
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

#  The store opens at middday and closes at 6PM each day.
time_slots = (
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
)

# Status of the bookings
status_options = (
    ('Awaiting confirmation', 'Awaiting confirmation'),
    ('Booking accepted', 'Booking accepted'),
    ('Booking declined', 'Booking declined'),
    ('Booking expired', 'Booking expired'),
)


class Slot(models.Model):
    """
    a class for the slot model
    """
    slot_id = models.AutoField(primary_key=True)
    slot_name = models.CharField(
        max_length=50, default='New Slot', unique=True)
    max_slots = models.PositiveIntegerField(default=2)

    class Meta:
        ordering = ['-max_slots']

    def __str__(self):
        return self.slot_name


class Booking(models.Model):
    """
    a class for the booking model
    """
    booking_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=25, choices=time_slots, default='10:00')
    slot = models.ForeignKey(
        Slot, on_delete=models.CASCADE, related_name="slot_reserved",
        null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=200, default="")
    phone = PhoneNumberField(null=True)
    status = models.CharField(
        max_length=25, choices=status_options, default='awaiting confirmation')
    slots = (
        (1, "1 guest"),
        (2, "2 guests"),
        (3, "3 guests"),
        (4, "4 guests"),
        (5, "5 guests"),
    )
    guest_count = models.IntegerField(choices=slots, default=2)

    class Meta:
        """
        A class to order
        the times of requested slots
        and a function to ensure there is no double
        bookings.
        """
        ordering = ['-requested_time']
        unique_together = ('requested_date', 'requested_time', 'slot')

    def __str__(self):
        return self.status
