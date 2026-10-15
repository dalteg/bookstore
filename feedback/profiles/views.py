from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import UserProfile


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = ("image",)
    success_url = reverse_lazy("profiles:profile-list")


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"