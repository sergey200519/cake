from typing import Any
from django.db import models

from authapp.models import User

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
    description = models.TextField(verbose_name="Описание", null=True)

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


    rating = models.FloatField(null=True, blank=True, default=0)
    summ_rating = models.FloatField(null=True, blank=True, default=0)
    count_reviews = models.PositiveIntegerField(null=True, blank=True, default=0)


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











class ExclusiveCategories(models.Model):

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    

class ExclusiveProducts(models.Model):

    name = models.TextField(verbose_name="Название")
    ingredients = models.CharField(verbose_name="Ингредиенты", max_length=128)
    category = models.ForeignKey(ExclusiveCategories, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    article = models.PositiveIntegerField(verbose_name="Артиул", unique=True)


    def __str__(self):
        return f"{self.name} | {self.category}"

class ImgExclusive(models.Model):
    image = models.ImageField(upload_to='cakes_images', verbose_name="Фото", blank=True)
    exclusive = models.ForeignKey(ExclusiveProducts, verbose_name="эксклюзив", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'Фото к "{self.exclusive}"'








class SwiperSlides(models.Model):
    img = models.ImageField(upload_to='slides_images', verbose_name="Фото", blank=True)
    title = models.TextField(verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")


class Reviews(models.Model):
    ACTIVE = 'active'
    NOTACTIVE = 'notactive'

    STATUS_CHOICES = (
        (ACTIVE,'активен'),
        (NOTACTIVE,'не активен'),
    )
    status = models.CharField(verbose_name='статус',choices=STATUS_CHOICES,blank=True, max_length=9, default=STATUS_CHOICES[1])
    
    rating = models.FloatField(null=True, blank=True, default=0)
    text = models.TextField(verbose_name="Коментарий")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    new = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        summ = 0
        temp_count = 0
        for item in Reviews.objects.all():
            if item.status == "active" and item.product == self.product:
                summ += item.rating
                temp_count += 1
        self.product.summ_rating = summ
        self.product.count_reviews = temp_count
        if temp_count == 0:
            self.product.rating = 0
        else:
            self.product.rating = self.product.summ_rating / self.product.count_reviews
            
        self.product.save()

    # def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]:
    #     print("drtyh ->")
    #     super().delete(using, keep_parents)
    #     print("end <-")
    #     summ = 0
    #     temp_count = 0
    #     for item in Reviews.objects.all():
    #         if item.status == "active" and item.product == self.product:
    #             summ += self.rating
    #             temp_count += 1
    #     self.product.summ_rating = summ
    #     self.product.count_reviews = temp_count
    #     try:
    #         self.product.rating = self.product.summ_rating / self.product.count_reviews
    #     except:
    #         self.product.rating = 0
    #     self.product.save()


    

