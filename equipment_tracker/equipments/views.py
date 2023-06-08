from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from equipment_tracker.equipments.models import Stock, Warehouse


class StockCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """Creates a stock item"""

    # required perm for the view
    permission_required: str = "equipments.add_stock"

    model = Stock
    fields = [
        "name",
        "description",
    ]
    template_name = "equipments/stock/create_equipment.html"
    success_message = _("Stock successfully created")

    def get_success_url(self):
        return reverse_lazy("equipments:list_stock")


create_stock_view = StockCreateView.as_view()


class ListStockView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """List stock"""

    permission_required: str = "equipments.view_stock"
    model = Stock
    paginate_by = 15
    template_name = "equipments/stock/list_stock.html"


list_stock_view = ListStockView.as_view()


class UpdateStockView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """Updates source"""

    # required perm for the view
    permission_required: str = "equipments.change_stock"
    model = Stock
    fields = [
        "name",
        "description",
    ]
    template_name = "equipments/stock/update_stock.html"
    success_message = _("Stock successfully updated")

    def get_success_url(self):
        return reverse_lazy("equipments:list_stock")


update_stock_view = UpdateStockView.as_view()


class WarehouseCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """Creates a warehouse item"""

    # required perm for the view
    permission_required: str = "equipments.add_warehouse"

    model = Warehouse
    fields = ["name", "description", "district"]
    template_name = "equipments/warehouse/create_warehouse.html"
    success_message = _("Warehouse successfully added")

    def get_success_url(self):
        return reverse_lazy("equipments:list_warehouse")


create_warehouse_view = WarehouseCreateView.as_view()


class ListWarehouseView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """List stock"""

    permission_required: str = "equipments.list_warehouse"
    model = Warehouse
    paginate_by = 15
    template_name = "equipments/warehouse/list_warehouse.html"


list_warehouse_view = ListWarehouseView.as_view()


class UpdateWarehouseView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """Updates warehouse item"""

    # required perm for the view
    permission_required: str = "equipments.change_warehouse"
    model = Warehouse
    fields = [
        "name",
        "description",
        "district",
    ]
    template_name = "equipments/warehouse/update_warehouse.html"
    success_message = _("Warehouse successfully updated")

    def get_success_url(self):
        return reverse_lazy("equipments:list_warehouse")


update_warehouse_view = UpdateWarehouseView.as_view()
