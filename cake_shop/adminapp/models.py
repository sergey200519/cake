from django.db import models

# Create your models here.
class Applications(models.Model):
    user_name = models.CharField(max_length=800)
    email = models.EmailField(unique=True, blank=True, verbose_name="Электроная почта")
    report = models.TextField()