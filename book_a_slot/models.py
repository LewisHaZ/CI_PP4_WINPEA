from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

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
    ('awaiting confirmation', 'awaiting confirmation'),
    ('booking accepted', 'booking accepted'),
    ('booking declined', 'booking declined'),
    ('booking expired', 'booking expired'),
)


class Slot(models.Slot):
    """
    a class for the slot model
    """
    slot_id = models.AutoField(primary_key=True)
    slot_name = models.CharField(
        max_length=50, default='New Slot', unique=True)
    max_slots = models.IntegerField()

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
        User, on_delete=models.CASCADE, related_name='user', null=True)
    status = models.CharField(
        max_length=25, choices=status_options, default='awaiting confirmation',
        unique=True)

    class Meta:
        ordering = ['-requested_time']

    def __str__(self):
        return self.booking_id


class User(models.Model):
    """
    a class for the User model
    """
    user_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254, default="")
    phone =

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user_id
