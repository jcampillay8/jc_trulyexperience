from django.urls import path
from . import views


urlpatterns = [

    path("", views.fintech_funding, name="fintech_funding"),
    path("fintech_funding_add", views.fintech_funding_add, name="fintech_funding_add"),
    path("fintech_funding_edit/<int:id>", views.fintech_funding_edit, name="fintech_funding_edit"),
    path("fintech_funding_delete/<int:id>", views.fintech_funding_delete, name="fintech_funding_delete"),
    path('fintech_Data_Dashboard/', views.search_fintech_funding, name='search_fintech_funding'),
    
]
