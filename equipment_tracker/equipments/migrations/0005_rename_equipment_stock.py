# Generated by Django 4.1.9 on 2023-06-07 11:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("equipments", "0004_warehouse_remove_equipment_serial_number_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Equipment",
            new_name="Stock",
        ),
    ]
