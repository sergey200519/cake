from django.urls import path
from mainapp.views import index, ProductDetail, add_review

app_name = "mainapp"
urlpatterns = [
    path("", index, name="index"),
    path("detail/<int:pk>/", ProductDetail.as_view(), name="detail"),
    path("add_review/<int:pk>/", add_review, name="add_review")
]