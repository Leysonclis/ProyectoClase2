from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Contacto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_contacto