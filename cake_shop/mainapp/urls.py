from django.urls import path
from mainapp.views import index, ProductDetail

app_name = "mainapp"
urlpatterns = [
    path("", index, name="index"),
    path("detail/<int:pk>/", ProductDetail.as_view(), name="detail"),
]