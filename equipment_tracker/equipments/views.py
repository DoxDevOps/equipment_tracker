from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView

from equipment_tracker.equipments.models import Stock


class StockCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """Creates a stock item"""

    # required perm for the view
    permission_required: str = "equipments.add_stock"

    model = Stock
    fields = [
        "name",
        "description",
    ]
    template_name = "equipments/create_equipment.html"
    success_message = _("Stock successfully created")


create_stock_view = StockCreateView.as_view()
