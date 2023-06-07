from django.utils.translation import pgettext_lazy


class ItemLocation:
    """Some ops depend on this data for a member obj"""

    WAREHOUSE = "Warehouse"
    FACILITY = "Facility"

    CHOICES = [
        (WAREHOUSE, pgettext_lazy("item location", "Warehouse")),
        (FACILITY, pgettext_lazy("item location", "Facility")),
    ]
