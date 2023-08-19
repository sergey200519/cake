from django.urls import path
from mainapp.views import index

from authapp.views import login

app_name = 'authapp'
urlpatterns = [
    path("login/", login, name="login"),
]