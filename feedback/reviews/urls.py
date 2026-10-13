from django.urls import path
from . import views

urlpatterns = [
    path("reviews/create/", views.ReviewView.as_view(), name="create-review"),
    path("thank_you/", views.ThankYouView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="single-review")
]