# Generated by Django 4.2.4 on 2023-12-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Applications",
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
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="Электроная почта"
                    ),
                ),
                ("report", models.TextField()),
                ("times_send", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
