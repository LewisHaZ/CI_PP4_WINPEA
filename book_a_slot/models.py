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
