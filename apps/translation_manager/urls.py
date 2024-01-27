from django.urls import path
from . import views

urlpatterns = [
    path('', views.translation_manager, name='translation_manager'),
    path("translation_manager_add", views.translation_manager_add, name="translation_manager_add"),
    path("translation_manager_edit/<int:id>", views.translation_manager_edit, name="translation_manager_edit"),
    path("translation_manager_delete/<int:id>", views.translation_manager_delete, name="translation_manager_delete"),
    path('expenses/search_translation_manager', views.search_translation_manager, name='search_translation_manager'),
]
