from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "review/review.html",{
            "form":form})

    def post(self,request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you/")

        return render(request, "review/review.html",{
                    "form":form})



def thank_you(request):
     return render(request, "review/thank_you.html")