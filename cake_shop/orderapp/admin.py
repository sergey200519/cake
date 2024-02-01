from django.contrib import admin

from orderapp.models import Order, OrderProduct, PromoCode

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(PromoCode)