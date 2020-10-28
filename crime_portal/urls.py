from django.contrib import admin
from django.urls import path, include

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', include('userDashboard.urls')),
    path('', include('userDashboard.urls')),
    path('administrator/', include('adminDashboard.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('userDashboard.api.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)