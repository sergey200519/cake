# Generated by Django 4.2.4 on 2024-01-18 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("basketapp", "0010_basketproducts_weight_gram"),
        ("orderapp", "0003_alter_order_email_alter_order_phone_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orderapp.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="basketapp.basketproducts",
                    ),
                ),
            ],
        ),
    ]
