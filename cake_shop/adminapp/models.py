from django.db import models

# Create your models here.
class Applications(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField(blank=True, verbose_name="Электроная почта")
    report = models.TextField()
    times_send = models.DateTimeField(auto_now_add=True)