from django.urls import path
from mainapp.views import index

from authapp.views import login, register, logout, profile_edit, UserPasswordChangeView

app_name = 'authapp'
urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("profile/", profile_edit, name="profile"),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
]