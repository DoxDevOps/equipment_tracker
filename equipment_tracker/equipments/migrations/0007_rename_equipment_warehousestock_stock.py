# Generated by Django 4.1.9 on 2023-06-07 11:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("equipments", "0006_facility_facilitystock"),
    ]

    operations = [
        migrations.RenameField(
            model_name="warehousestock",
            old_name="equipment",
            new_name="stock",
        ),
    ]
