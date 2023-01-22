from django.contrib import admin
from django.urls import path
from .views import HomePageView,DetailsPageView,RegisterPageView

app_name = "stdetails"

urlpatterns = [
    path('',HomePageView.as_view()),
    path('details',DetailsPageView.as_view()),
    path('register',RegisterPageView.as_view())
]
