from django.contrib import admin

from mainapp.models import ProductCategories, Products, ImgProducts

# Register your models here.
admin.site.register(ProductCategories)
admin.site.register(Products)
admin.site.register(ImgProducts)
