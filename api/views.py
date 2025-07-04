# api/views.py
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    """
    Este ViewSet proporciona automáticamente las acciones de
    `list` (listar todos), `create` (crear), `retrieve` (ver uno),
    `update` (actualizar) y `destroy` (eliminar).
    """
    # Le decimos qué conjunto de datos debe manejar: todos los pacientes,
    # ordenados por fecha de creación (los más nuevos primero).
    queryset = Patient.objects.all().order_by('-created_at')
    
    # Le decimos qué "traductor" (serializer) debe usar.
    serializer_class = PatientSerializer