from django.urls import path
from mainapp.views import index

from authapp.views import login, register, logout, profile_edit

app_name = 'authapp'
urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("profile/", profile_edit, name="profile")
]