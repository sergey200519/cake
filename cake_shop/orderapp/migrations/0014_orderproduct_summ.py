# Generated by Django 4.2.4 on 2024-01-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderapp", "0013_orderproduct_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderproduct",
            name="summ",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]