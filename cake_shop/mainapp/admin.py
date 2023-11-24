from django.contrib import admin

from mainapp.models import ProductCategories, Products, ImgProducts, SwiperSlides, Reviews, ReviewsImgs


# Register your models here.
admin.site.register(ProductCategories)
admin.site.register(Products)
admin.site.register(ImgProducts)
admin.site.register(SwiperSlides)
admin.site.register(Reviews)
admin.site.register(ReviewsImgs)