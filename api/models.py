# api/models.py
from django.db import models

class Patient(models.Model):
    # Este es el ID que verá el usuario en la interfaz, como "P2024-001".
    # Lo generaremos automáticamente.
    patient_id = models.CharField(max_length=20, unique=True, blank=True)
    
    # Campos para la información del paciente.
    name = models.CharField(max_length=200, verbose_name="Nombre Completo")
    dob = models.DateField(verbose_name="Fecha de Nacimiento")
    contact = models.EmailField(max_length=100, verbose_name="Email de Contacto")
    
    # Campos de fecha que se actualizan solos.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Esta función se ejecuta cada vez que guardamos un paciente.
    # La usamos para crear el 'patient_id' de forma automática.
    def save(self, *args, **kwargs):
        if not self.id and not self.patient_id:
            # Busca el último paciente para saber qué número sigue.
            last_patient = Patient.objects.all().order_by('id').last()
            last_id = 0
            if last_patient:
                last_id = last_patient.id
            
            # Crea el nuevo ID, por ejemplo: "P2024-001", "P2024-002", etc.
            self.patient_id = f"P2024-{(last_id + 1):03d}"
        
        super(Patient, self).save(*args, **kwargs)

    # Esto define cómo se mostrará un paciente en el panel de administrador de Django.
    def __str__(self):
        return f"{self.patient_id} - {self.name}"