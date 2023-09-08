from django.db import models

# Create your models here.
class Applications(models.Model):
    email = models.EmailField(unique=True, blank=True, verbose_name="Электроная почта")
    report = models.TextField()
    times_send = models.DateTimeField(auto_now_add=True)