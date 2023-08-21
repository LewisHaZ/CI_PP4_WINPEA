# 3rd Party Imports
from django.db import models


ITEM_TYPE = (
    (0, 'Necklaces'), (1, 'Bags'), (2, 'Rings'), (3, 'Bracelets'), (4, 'New'))


# Model for Items
class ProductItem(models.Model):
    """
    a class for the product item model
    """
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(
        max_length=50,
        unique=True
        )
    description = models.CharField(
        max_length=200,
        unique=True
        )
    price = models.FloatField()
    item_type = models.IntegerField(
        choices=ITEM_TYPE,
        default=4
        )
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-item_type']

    def __str__(self):
        return self.item_name
