from django.conf.urls.static import static

from IsMDb import settings
from .admin import admin_site
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', admin_site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)