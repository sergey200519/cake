# Generated by Django 4.2.4 on 2024-01-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="applications",
            name="username",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]