# Generated by Django 4.2.4 on 2024-02-06 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderapp", "0021_alter_order_summ_alter_order_total_summ"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="summ",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
        migrations.AlterField(
            model_name="order",
            name="total_summ",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
    ]
