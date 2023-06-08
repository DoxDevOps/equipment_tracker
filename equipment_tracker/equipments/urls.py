from django.urls import path

from equipment_tracker.equipments import views

app_name = "equipments"


# sources
urlpatterns = [
    path("stock/create", view=views.create_stock_view, name="create-stock"),
    path("stock/list", view=views.list_stock_view, name="list_stock"),
    path("stock/update/<int:pk>", view=views.update_stock_view, name="update_stock"),
    path("warehouse/create", view=views.create_warehouse_view, name="create-warehouse"),
    path("warehouse/list", view=views.list_warehouse_view, name="list_warehouse"),
    path("warehouse/update/<int:pk>", view=views.update_warehouse_view, name="update_warehouse"),
]
