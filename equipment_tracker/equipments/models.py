from django.db import models

from equipment_tracker.common.base import BaseModel

from . import ItemLocation

# Create your models here.


class Equipment(BaseModel):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    serial_number = models.CharField(max_length=50, null=True)


class Location(models.CharField):
    name = models.CharField(
        null=False,
        choices=ItemLocation.CHOICES,
        default=ItemLocation.WAREHOUSE,
    )
