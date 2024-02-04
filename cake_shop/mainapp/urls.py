from django.urls import path
from mainapp.views import index, ProductDetail, add_review, exclusive, ExclusiveDetail, application_add, \
    about_us, partners, videos, contacts, \
    offer, personalization, requisites

app_name = "mainapp"
urlpatterns = [
    path("", index, name="index"),
    path("detail/<int:pk>/", ProductDetail.as_view(), name="detail"),
    path("add_review/<int:pk>/", add_review, name="add_review"),

    path("exclusive/", exclusive, name="exclusive"),
    path("detail_ex/<int:pk>/", ExclusiveDetail.as_view(), name="detail_ex"),

    path("application_add/", application_add, name="application_add"),

    path("about_us/", about_us, name="about_us"),
    path("partners/", partners, name="partners"),
    path("videos/", videos, name="videos"),
    path("contacts/", contacts, name="contacts"),

    path("offer/", offer, name="offer"),
    path("personalization/", personalization, name="personalization"),
    path("requisites/", requisites, name="requisites")
]