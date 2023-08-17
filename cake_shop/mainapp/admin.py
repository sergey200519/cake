from django.contrib import admin

# Register your models here.
from mainapp.models import ProductCategories, Products, ImgProducts

admin.site.register(ProductCategories)
admin.site.register(Products)
admin.site.register(ImgProducts)