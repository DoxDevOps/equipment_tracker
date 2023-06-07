from django.db import models

from equipment_tracker.common.base import BaseModel

from . import Itemlocation

# Create your models here.


class Equipment(BaseModel):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    serial_number = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100, null=True, choices=Itemlocation.LOCATION_CHOICES)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
