from rest_framework import serializers
from .models import Empleado, EstadoEmpleado, Deducciones, Devengado, NovedadDeducciones,NovedadDevengado, Nomina, Contrato, TipoContrato, HorasExtras

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = "__all__"
        
class EstadoEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoEmpleado
        fields = "__all__"
        
class DevengadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devengado
        fields = "__all__"
        
        
class NovedadDevengadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovedadDevengado
        fields = "__all__"
        
class DeduccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deducciones
        fields = "__all__"
        
class NovedadDeduccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovedadDeducciones
        fields = "__all__"

class NominaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomina
        fields = "__all__"
                
class TipoContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContrato 
        fields = "__all__"
        
class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = "__all__"
        
class HorasExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorasExtras
        fields = "__all__"