from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Viaje(models.Model):
    OPCIONES_ORIGEN = [
        ('porteria_25', 'Portería de la 25'),
        ('porteria_principal', 'Portería principal'),
        ('porteria_30', 'Portería de la 30'),
    ]
    TIPOS_VEHICULO = [
        ('carro', 'Carro'),
        ('moto', 'Moto'),
        ('otro', 'Otro'),
    ]
    conductor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viajes_publicados')
    origen = models.CharField(max_length=30, choices=OPCIONES_ORIGEN)
    destino = models.CharField(max_length=100)
    tipo_vehiculo = models.CharField(max_length=10, choices=TIPOS_VEHICULO)
    fecha = models.DateTimeField(auto_now_add=True)
    hora = models.TimeField(default='00:00')
    asientos_disponibles = models.PositiveIntegerField()

    def clean(self):
        # Solo "carro" puede tener hasta 4 asientos, los demás solo 1
        if self.tipo_vehiculo == 'carro':
            if self.asientos_disponibles > 4:
                raise ValidationError("Un carro puede tener máximo 4 asientos disponibles.")
        else:
            if self.asientos_disponibles > 1:
                raise ValidationError("Solo un carro puede tener más de 1 asiento disponible.")

    def __str__(self):
        return f"{self.get_origen_display()} a {self.destino} ({self.fecha})"

class ViajeTomado(models.Model):
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE, related_name='tomados')
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    contacto = models.CharField(max_length=50)

    def __str__(self):
        if self.usuario:
            return f"{self.usuario.username} tomó {self.viaje}"
        return f"Anónimo tomó {self.viaje}"