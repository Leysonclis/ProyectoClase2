from rest_framework import serializers
from .models import Viaje, ViajeTomado

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'

    def validate(self, data):
        tipo_vehiculo = data.get('tipo_vehiculo')
        asientos = data.get('asientos_disponibles')
        if tipo_vehiculo == 'carro' and asientos > 4:
            raise serializers.ValidationError("Un carro puede tener máximo 4 asientos disponibles.")
        if tipo_vehiculo != 'carro' and asientos != 1:
            raise serializers.ValidationError("Solo puedes poner 1 asiento disponible para moto u otro vehículo.")
        return data

class ViajeTomadoSerializer(serializers.ModelSerializer):
    tipo_vehiculo = serializers.CharField(source='viaje.tipo_vehiculo', read_only=True)
    asientos_disponibles = serializers.IntegerField(source='viaje.asientos_disponibles', read_only=True)

    class Meta:
        model = ViajeTomado
        fields = ['id', 'viaje', 'usuario', 'contacto', 'tipo_vehiculo', 'asientos_disponibles']