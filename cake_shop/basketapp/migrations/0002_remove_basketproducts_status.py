# Generated by Django 4.2.4 on 2024-01-13 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("basketapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="basketproducts",
            name="status",
        ),
    ]
