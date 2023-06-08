from django.db import models
from django.utils.translation import gettext_lazy as _

from equipment_tracker.common.base import BaseModel


class Stock(BaseModel):
    """Item or material"""

    name = models.CharField(max_length=100, blank=False, help_text="The name of the equipment", null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Warehouse(BaseModel):
    """Stores equipment"""

    name = models.CharField(max_length=100, blank=False, help_text="The name of the warehouse")
    description = description = models.TextField()
    district = models.CharField(max_length=50, default="Lilongwe")


class WarehouseStock(BaseModel):
    """Stock at a warehouse"""

    stock = models.ForeignKey("Stock", on_delete=models.CASCADE)
    warehouse = models.ForeignKey("Warehouse", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Quantity"), blank=False)


class Facility(BaseModel):
    """Health facility"""

    name = models.CharField(max_length=100, blank=False, help_text="The name of the facility")


class FacilityStock(BaseModel):
    """Stock at a facility"""

    stock = models.ForeignKey("Stock", on_delete=models.CASCADE)
    facility = models.ForeignKey("Facility", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Quantity"), blank=False)
