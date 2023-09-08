from django.urls import path
from basketapp.views import basket, basket_add, basket_remove



app_name = "basketapp"
urlpatterns = [
    path("", basket, name="basket"),
    path("add/<int:id>/",basket_add,name="basket_add"),
    path("remove/<int:basket_id>",basket_remove,name="basket_remove")
]