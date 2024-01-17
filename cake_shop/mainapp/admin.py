from django.contrib import admin

from mainapp.models import ProductCategories, SwiperSlides, \
    Reviews, ExclusiveCategories, \
    BaseProduct, Product, ImgProduct, \
    ExclusiveProducts, ImgExclusive


# Register your models here.
admin.site.register(ProductCategories)

admin.site.register(ExclusiveCategories)
admin.site.register(ExclusiveProducts)
admin.site.register(ImgExclusive)



admin.site.register(SwiperSlides)
admin.site.register(Reviews)

admin.site.register(BaseProduct)
admin.site.register(Product)
admin.site.register(ImgProduct)