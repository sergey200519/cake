from django.contrib import admin

from mainapp.models import ProductCategories, Products, ImgProducts, SwiperSlides, \
    Reviews, ExclusiveCategories, ExclusiveProducts, ImgExclusive


# Register your models here.
admin.site.register(ProductCategories)
admin.site.register(Products)

admin.site.register(ExclusiveCategories)
admin.site.register(ExclusiveProducts)
admin.site.register(ImgExclusive)



admin.site.register(ImgProducts)
admin.site.register(SwiperSlides)
admin.site.register(Reviews)