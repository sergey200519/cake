# Generated by Django 4.2.4 on 2024-01-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0012_remove_exclusiveproducts_article_and_more"),
        ("orderapp", "0006_order_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderproduct",
            name="count",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderproduct",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="basket_product_images",
                verbose_name="Фото",
            ),
        ),
        migrations.AddField(
            model_name="orderproduct",
            name="weight_gram",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="orderproduct",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="mainapp.baseproduct"
            ),
        ),
    ]