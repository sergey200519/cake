from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="user_img", blank=True, verbose_name="Фото")
    phone = PhoneNumberField(unique=True, blank=True, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, blank=True, verbose_name="Электроная почта")