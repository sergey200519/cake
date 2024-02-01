from django.db import models

from authapp.models import User

# Create your models here.
class BasketProducts(models.Model):
    
    image = models.ImageField(upload_to="basket_product_images", verbose_name="Фото", null=True, blank=True)
    name = models.TextField(verbose_name="Название")
    count = models.PositiveIntegerField()
    weight = models.FloatField(default=0)
    weight_gram = models.FloatField(default=0)
    price = models.FloatField()
    summ = models.FloatField(default=0)

    
    article = models.IntegerField()

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    @staticmethod
    def get_count(user):
        count = 0
        # TODO: make filter
        for item in BasketProducts.objects.all():
            if  item.user == user:
                count += item.count
        return count
    
    @staticmethod
    def get_total_price(user):
        price = 0
        for item in BasketProducts.objects.filter(user=user):
            price += item.price * item.count
        return price

    def save(self, *args, **kwargs):
        
        self.summ = self.price * self.count
        
        self.weight_gram = self.weight / 1000

        super().save(*args, **kwargs)
