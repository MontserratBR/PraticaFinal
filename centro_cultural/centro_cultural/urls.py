from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('app_gestion_actividades.urls')),
]
