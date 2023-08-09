from django.db import models

# Create your models here.
class Cakes(models.Model):
    title = models.TextField(verbose_name="название", blank=True, unique=True)
    image = models.ImageField(verbose_name="фото", upload_to='cakes_images', blank=True)
    ingredients = models.CharField(verbose_name="ингредиенты", max_length=128)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    price = models.DecimalField(verbose_name="цена", max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "Торты"