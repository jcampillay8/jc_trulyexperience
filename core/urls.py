from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from apps.Error_Handler.views import Error404View, Error505View

urlpatterns = [
    path("", include("apps.home.urls")),
    path("authentication/", include("apps.authentication.urls")),
    path('guest_user/', include('guest_user.urls')),
    path('professional_studies/', include("apps.Professional_Studies.urls")),
    path('contact/',include("apps.contact.urls")),
    path('about_me/',include("apps.blog.urls")),
    path('portfolio/',include("apps.portfolio.urls")),
    path('Quizzes/',include("apps.Quizzes.urls")),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    #path('translation_manager/',include("apps.translation_manager.urls")),
    path('Fintech_Data_Dashboard/',include("apps.Opportunity_Data_Journey.Fintech_Data_Dashboard.urls")),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = Error404View.as_view()

handler505 = Error505View.as_error_view()