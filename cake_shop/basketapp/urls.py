from django.urls import path
from basketapp.views import product_add_basket, exclusive_add_basket, delete_basket_product

app_name = "mainapp"
urlpatterns = [
    path("product_add_basket/", product_add_basket, name="product_add_basket"),
    path("exclusive_add_basket/", exclusive_add_basket, name="exclusive_add_basket"),
    path("delete_basket_product/<int:pk>/", delete_basket_product, name="delete_basket_product")
]