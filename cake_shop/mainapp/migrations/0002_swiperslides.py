# Generated by Django 4.2.4 on 2023-10-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SwiperSlides",
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
                    "img",
                    models.ImageField(
                        blank=True, upload_to="slides_images", verbose_name="Фото"
                    ),
                ),
                ("title", models.TextField(verbose_name="Заголовок")),
                ("description", models.TextField(verbose_name="Описание")),
            ],
        ),
    ]
