from django.db import models

# Create your models here.
class ProductCategories(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.TextField(verbose_name="Название", blank=True, unique=True)
    ingredients = models.CharField(verbose_name="Ингредиенты", max_length=128)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=0)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE, verbose_name="Категория")

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