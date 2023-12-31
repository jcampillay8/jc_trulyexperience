from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("apps.home.urls")),
    path("authentication/", include("apps.authentication.urls")),
    path('guest_user/', include('guest_user.urls')),
    path('professional_studies/', include("apps.Professional_Studies.urls")),
    path('contact/',include("apps.contact.urls")),
    path('blog/',include("apps.blog.urls")),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
