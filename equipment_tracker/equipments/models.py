from django.db import models

from equipment_tracker.common.base import BaseModel

# Create your models here.


class Equipment(BaseModel):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    serial_number = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
