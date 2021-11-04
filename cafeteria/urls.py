from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings

urlpatterns = [
    # PATH Admin
    path('admin/', admin.site.urls),
    # PATH core
    path('', include('core.urls') ),
    # PATH services
    path('services/',include('services.urls') ),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
