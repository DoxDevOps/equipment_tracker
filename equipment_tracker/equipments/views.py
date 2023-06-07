import logging

from django.db import transaction
from rest_framework import viewsets

from equipment_tracker.equipments.models import Stock, WarehouseStock


class StockViewSet(viewsets.ModelViewSet):
    """Stock viewset"""

    queryset = Stock.objects.all().order_by("-created_at")
    http_method_names = ["get", "post"]

    def get_queryset(self):
        """Filter by owner"""
        stock = Stock.objects.filter(created_by=self.request.user).order_by("-created_at")
        return stock

    def perform_create(self, stock_data):
        with transaction.atomic():
            stock_data["created_by"] = self.request.user
            stock = Stock.objects.create(**stock_data)

            # Update warehouse stock quantity to reflect the added item
            warehouse = stock.warehouse
            warehouse_stock, created = WarehouseStock.objects.get_or_create(
                stock=stock, warehouse=warehouse, defaults={"quantity": 0}
            )
            warehouse_stock.quantity += stock.quantity
            warehouse_stock.save()

            logging.info(f"Successfully created stock {stock.id} for warehouse {warehouse.id}")
