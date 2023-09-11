from django.db import models

from authapp.models import User
from mainapp.models import Products

# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user} | {self.product.name} | {self.quantity}"
    

    def sum(self):
        return self.quantity * self.product.price

    def get_basket(self):
        return Basket.objects.filter(user=self.user)

    def total_sum(self):
        print("sum")
        baskets = self.get_basket()
        return sum(basket.sum() for basket in baskets)

    def total_quantity(self):
        print("qqqqqqqqqqqqqqqqqqqqqqqqqq")
        baskets = self.get_basket()
        return sum(basket.quantity for basket in baskets)
