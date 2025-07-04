# api/serializers.py
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        # Aquí definimos los campos del modelo que queremos "traducir".
        # Usamos el 'id' de Django como clave principal para la API
        # y 'patient_id' como el identificador que ve el usuario.
        fields = ['id', 'patient_id', 'name', 'dob', 'contact', 'created_at']
        
        # Hacemos que ciertos campos sean de solo lectura para que no se puedan
        # modificar directamente a través de la API.
        read_only_fields = ['patient_id', 'created_at']