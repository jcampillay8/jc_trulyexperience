from django.urls import path
from . import views

urlpatterns = [
    path('', views.professional_studies, name="professional_studies"),
    path('add/', views.add_professional_studies, name="add_professional_studies"),
]
