from pathlib import Path

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ProfileForm


def store_file(file):
    storage = FileSystemStorage(location=settings.MEDIA_ROOT)
    return storage.save(Path(file.name).name, file)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(
            request,
            "profiles/create_profile.html",
            {"form": form},
        )

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(
                request,
                "profiles/create_profile.html",
                {"form": form},
                status=400,
            )

        store_file(form.cleaned_data["user_image"])
        return HttpResponseRedirect("/")