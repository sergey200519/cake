from typing import Any
from django.db import models

from authapp.models import User

# Create your models here.











































class SwiperSlides(models.Model):
    img = models.ImageField(upload_to='slides_images', verbose_name="Фото", blank=True)
    title = models.CharField(verbose_name="Заголовок", max_length=1000)
    description = models.CharField(verbose_name="Описание", max_length=1000)


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
    # product = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)
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

class BasketProducts(models.Model):
    image = models.ImageField(upload_to="basket_product_images", verbose_name="Фото", blank=True)
    name = models.TextField(verbose_name="Название")
    
