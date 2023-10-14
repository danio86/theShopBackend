from django.urls import path
from sales import views

urlpatterns = [
    path('sales/', views.SoldList.as_view()),
    path('sales/<int:pk>/', views.SoldDetail.as_view()),
]