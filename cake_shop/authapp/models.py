from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    MALE = "M"
    FEMALE = "W"

    GENDER_CHOICES = (
        (MALE,"Мужской"),
        (FEMALE,"Женский"),
    )

    image = models.ImageField(upload_to='users_image', null=True, blank=True)

    phone = PhoneNumberField(unique=True, blank=True, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, blank=True, verbose_name="Электроная почта")
    gender = models.CharField(verbose_name='пол',choices=GENDER_CHOICES,blank=True,max_length=10)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождение")
    address = models.CharField(verbose_name="Адресс", blank=True, max_length=200)
    patronymic = models.CharField(verbose_name="Отчество", max_length=150)


class ImgUser(models.Model):
    image = models.ImageField(upload_to='users_img', verbose_name="Фото", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
