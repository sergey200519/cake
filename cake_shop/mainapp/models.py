from django.db import models

# Create your models here.
class ProductCategories(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.TextField(verbose_name="Название")
    ingredients = models.CharField(verbose_name="Ингредиенты", max_length=128)
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание", blank=True)

    article_four_hundred = models.PositiveIntegerField(verbose_name="Артиул 400г", unique=True)
    price_four_hundred = models.DecimalField(verbose_name="Цена 400г", max_digits=10, decimal_places=2)

    article_six_hundred = models.PositiveIntegerField(verbose_name="Артиул 600г", unique=True)
    price_six_hundred = models.DecimalField(verbose_name="Цена 600г", max_digits=10, decimal_places=2)

    article_eight_hundred = models.PositiveIntegerField(verbose_name="Артиул 800г", unique=True)
    price_eight_hundred = models.DecimalField(verbose_name="Цена 800г", max_digits=10, decimal_places=2)

    article_one_thousand = models.PositiveIntegerField(verbose_name="Артиул 1000г", unique=True)
    price_one_thousand = models.DecimalField(verbose_name="Цена 1000г", max_digits=10, decimal_places=2)

    article_two_thousand = models.PositiveIntegerField(verbose_name="Артиул 2000г", unique=True)
    price_two_thousand = models.DecimalField(verbose_name="Цена 2000г", max_digits=10, decimal_places=2)

    

    def __str__(self):
        return f"{self.name} | {self.category}"

    class Meta:
        verbose_name_plural = "Продукты"


class ImgProducts(models.Model):
    image = models.ImageField(upload_to='cakes_images', verbose_name="Фото", blank=True)
    product = models.ForeignKey(Products, verbose_name="Продукт", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'Фото к "{self.product}"'

    class Meta:
        verbose_name_plural = "Фото к продуктам"