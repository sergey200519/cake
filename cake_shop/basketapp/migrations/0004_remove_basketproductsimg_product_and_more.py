# Generated by Django 4.2.4 on 2024-01-13 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("basketapp", "0003_remove_basketproducts_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="basketproductsimg",
            name="product",
        ),
        migrations.DeleteModel(
            name="BasketProducts",
        ),
        migrations.DeleteModel(
            name="BasketProductsImg",
        ),
    ]
