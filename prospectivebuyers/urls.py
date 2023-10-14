from django.urls import path
from prospectivebuyers import views

urlpatterns = [
    path('prospectivebuyers/', views.ProspectivebuyerList.as_view()),
    path('prospectivebuyers/<int:pk>/', views.ProspectivebuyerDetail.as_view()),
]