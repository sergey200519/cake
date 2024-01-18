from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from basketapp.models import BasketProducts

# Create your models here.
class Order(models.Model):
    COMPLETED = "completed"
    NOTCOMPLETED = "notcompleted"
    CANCELLED = "cancelled"

    STATUS_CHOICES = (
        (COMPLETED, "завершенный"),
        (NOTCOMPLETED, "не завершенный"),
        (CANCELLED, "отменённый")
    )


    DELIVERY = "delivery"
    PICKUP = "pickup"
    DELIVERY_STATUS_CHOICES = (
        (DELIVERY, "доставка"),
        (PICKUP, "самовывоз")
    )


    status_completed = models.CharField(choices=STATUS_CHOICES, max_length=12, default=STATUS_CHOICES[1])
    status_delivery = models.CharField(choices=DELIVERY_STATUS_CHOICES, max_length=8)
    date = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField(default=0)
    summ = models.FloatField(default=0)
    promo_code = models.CharField(max_length=100, default=None)

    user_fullname = models.CharField(max_length=250, verbose_name="ФИО")
    phone = PhoneNumberField(verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электроная почта")

    index = models.CharField(max_length=50, default="С/в")
    city = models.CharField(max_length=500, default="С/в")
    street = models.CharField(max_length=250, default="С/в")
    num_house = models.CharField(max_length=50, default="С/в")
    num_flat = models.CharField(max_length=50, default="С/в")
    num_building =models.CharField(max_length=50, default="С/в")



class OrderProduct(models.Model):
    product = models.ForeignKey(BasketProducts, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
