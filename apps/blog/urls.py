from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog, name="blog"),
    path('add-blog/', views.add_blog, name="add_blog"),
    path('blog-detail/<slug>', views.blog_detail, name="blog_detail"),
    path('see-blog/', views.see_blog, name="see_blog"),
    path('blog-delete/<id>', views.blog_delete, name="blog_delete"),
    path('blog-update/<slug>/', views.blog_update, name="blog_update"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)