# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

# Esto crea un enrutador que automáticamente genera las URLs para nuestro ViewSet.
router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

# Las URLs de la API son ahora determinadas automáticamente por el enrutador.
urlpatterns = [
    path('', include(router.urls)),
]