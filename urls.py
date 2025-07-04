# lab_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Asegúrate de que 'include' esté importado

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Añade esta línea para conectar las URLs de nuestra app 'api'.
    # Todo lo que empiece con /api/ será manejado por nuestra API.
    path('api/', include('api.urls')), 
]