from .models import *
from rest_framework import serializers


class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = '__all__'

class TipoAulaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoAula
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):
    #zona = ZonaSerializer(many=True ,  read_only=True , source='zona_set')
    #tipo_aula= TipoAulaSerializer(read_only=True )
    class Meta:
        model = Aula
        fields = '__all__'
        #fields = ('id' , 'descripcion','estado','zona','tipo_aula')
    
    

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class DetalleAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleAcceso
        fields = '__all__'

class AccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acceso
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = '__all__'

class MqttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mqtt
        fields = '__all__'


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'


class HorarioPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioPersona
        fields = '__all__'




