# Generated by Django 4.2.4 on 2024-01-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderapp", "0012_alter_order_promo_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderproduct",
            name="name",
            field=models.TextField(default=1, verbose_name="Название"),
            preserve_default=False,
        ),
    ]
