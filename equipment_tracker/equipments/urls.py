from django.urls import path

from equipment_tracker.equipments import views

app_name = "equipments"


# sources
urlpatterns = [
    path("stock/create", view=views.create_stock_view, name="create-stock"),
]
