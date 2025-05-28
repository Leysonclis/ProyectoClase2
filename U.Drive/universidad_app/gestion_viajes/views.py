from rest_framework import generics, permissions
from .models import Viaje, ViajeTomado
from .serializers import ViajeSerializer, ViajeTomadoSerializer
from rest_framework import serializers

class PublicarViajeView(generics.CreateAPIView):
    serializer_class = ViajeSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save()

from rest_framework import generics, permissions, filters

class ListarViajesView(generics.ListAPIView):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ['tipo_vehiculo', 'destino', 'hora']  # <-- Agrega 'hora'

class TomarViajeView(generics.CreateAPIView):
    serializer_class = ViajeTomadoSerializer
    permission_classes = []

    def perform_create(self, serializer):
        viaje = serializer.validated_data['viaje']
        if viaje.asientos_disponibles < 1:
            raise serializers.ValidationError("No hay asientos disponibles en este viaje.")
        # Resta un cupo
        viaje.asientos_disponibles -= 1
        viaje.save()
        serializer.save(usuario=None)  # <-- Esto debe estar indentado aquí

class EliminarViajeView(generics.DestroyAPIView):
    queryset = Viaje.objects.all()
    permission_classes = []  # <--- Permite acceso sin autenticación
