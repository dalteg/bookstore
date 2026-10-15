from django.urls import path

from .views import CreateProfileView, ProfilesView

app_name = "profiles"

urlpatterns = [
    path("", CreateProfileView.as_view(), name="home"),
    path("profiles", CreateProfileView.as_view(), name="create-profile"),
    path("profiles/", CreateProfileView.as_view()),
    path("profiles/lists", ProfilesView.as_view(), name="profile-list"),
    path("profiles/lists/", ProfilesView.as_view()),
]
