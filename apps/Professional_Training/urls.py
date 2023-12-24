from django.urls import path
from . import views

urlpatterns = [
    path('', views.professional_training, name="professional_training"),
    path('add/', views.add_professional_training, name="add_professional_training"),
]
