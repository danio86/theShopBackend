from django.urls import path
from properties import views

urlpatterns = [
    path('properties/', views.PropertyList.as_view()),
]