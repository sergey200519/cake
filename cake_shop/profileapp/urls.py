from django.urls import path

from profileapp.views import ProfileListView, profile_edit

app_name = "profileapp"
urlpatterns = [
    path("", ProfileListView.as_view(), name="profile_list"),
    path("edit/<int:pk>/", profile_edit, name="profile_edit"),
]