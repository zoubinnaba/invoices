from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userprofile/', include('userprofile.urls')),
    path('client/', include('client.urls')),
    path('product/', include('product.urls')),
    path('invoice/', include('invoice.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)