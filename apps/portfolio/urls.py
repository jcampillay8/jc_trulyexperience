from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.portfolio_home, name="portfolio_home"),
    path('personal_projects/', views.personal_projects, name="personal_projects"),
    path('professional_projects/', views.professional_projects, name="professional_projects"),
    path('work_experience/', views.work_experience, name="work_experience"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
