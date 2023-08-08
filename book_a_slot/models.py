from django.db import models


# Create your models here.
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
    status = models.CharField(max_length=25, unique=True)

    class Meta:
        ordering = ['-requested_time']
  
    def __str__(self):
        return self.booking_id
  

class User(models.Model):
