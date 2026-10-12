from .forms import ReviewForm
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "review/review.html"
    success_url = "/thank_you/"


class ThankYouView(TemplateView):
    template_name = "review/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context

class ReviewListView(ListView):
    template_name = "review/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        return super().get_queryset().filter(rating__gt=4)


class SingleReviewView(DetailView):
    template_name = "review/single_review.html"
    model = Review
