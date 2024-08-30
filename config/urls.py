from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path("blog/", include("blog.urls", namespace="blog")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)