from django.urls import path
from inquiries import views

urlpatterns = [
    path('inquiries/', views.InquiryList.as_view()),
    path('inquiries/<int:pk>/', views.InquiryDetail.as_view())
]
