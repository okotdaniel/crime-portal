from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('userDashboard.urls')),
    path('', include('userDashboard.urls')),
    path('administrator/', include('adminDashboard.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('userDashboard.api.urls'))
]


