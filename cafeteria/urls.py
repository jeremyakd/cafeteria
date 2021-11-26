from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # PATH Admin
    path('admin/', admin.site.urls),
    # PATH blog
    path('blog/', include('blog.urls') ),
    # PATH core
    path('', include('core.urls') ),
    # PATH services
    path('services/',include('services.urls') ),
    # PATH pages
    path('page/', include('pages.urls') ),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
