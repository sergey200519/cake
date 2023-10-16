from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE,'М'),
        (FEMALE,'Ж'),
    )


    phone = PhoneNumberField(unique=True, blank=True, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, blank=True, verbose_name="Электроная почта")
    gender = models.CharField(verbose_name='пол',choices=GENDER_CHOICES,blank=True,max_length=2)
    date = models.DateField(auto_now=False, auto_now_add=True, blank=True) 