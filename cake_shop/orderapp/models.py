from django.db import models

from authapp.models import User

from mainapp.models import BaseProduct

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

    OWNER = "user"
    NOTOWNER = "admin"
    OWNER_STATUS = (
        (OWNER, "пользователь"),
        (NOTOWNER, "администратор")
    )

    status_completed = models.CharField(choices=STATUS_CHOICES, max_length=15)
    status_delivery = models.CharField(choices=DELIVERY_STATUS_CHOICES, max_length=8)
    status_owner = models.CharField(choices=OWNER_STATUS, max_length=15, default="user")
    date = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField(default=0)
    summ = models.FloatField(default=0)
    total_summ = models.FloatField(default=0)
    promo_code = models.CharField(max_length=100, default=None, blank=True, null=True)

    user_fullname = models.CharField(max_length=250, verbose_name="ФИО")
    phone = PhoneNumberField(verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электроная почта")

    index = models.CharField(max_length=50, default="С/в")
    region = models.CharField(max_length=50, default="С/в")
    city = models.CharField(max_length=500, default="С/в")
    street = models.CharField(max_length=250, default="С/в")
    num_house = models.CharField(max_length=50, default="С/в")
    num_flat = models.CharField(max_length=50, default="С/в")
    num_building = models.CharField(max_length=50, default="С/в")

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True, blank=True)

    def calculate_summ(self):
        for item in OrderProduct.objects.filter(order=self):
            self.summ += item.product.price * item.count
        self.total_summ = self.summ
        if self.promo_code != "" and PromoCode.objects.filter(promo_code=self.promo_code).exists():
            self.discount = PromoCode.objects.get(promo_code=self.promo_code).discount
            self.total_summ = float(self.summ) * (1 - float(self.discount) / 100)
            
        self.save()


class OrderProduct(models.Model):
    product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="basket_product_images", verbose_name="Фото", null=True, blank=True)
    name = models.TextField(verbose_name="Название")
    summ = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()
    weight_gram = models.FloatField(default=0)
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class PromoCode(models.Model):
    promo_code = models.CharField(max_length=50, unique=True)
    discount = models.FloatField(default=0)
    date = models.DateField(auto_now=False, auto_now_add=False)
