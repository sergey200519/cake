from django.urls import path
from mainapp.views import index, ProductDetail, add_review, exclusive, ExclusiveDetail

app_name = "mainapp"
urlpatterns = [
    path("", index, name="index"),
    path("detail/<int:pk>/", ProductDetail.as_view(), name="detail"),
    path("add_review/<int:pk>/", add_review, name="add_review"),

    path("exclusive", exclusive, name="exclusive"),
    path("detail_ex/<int:pk>/", ExclusiveDetail.as_view(), name="detail_ex"),
]