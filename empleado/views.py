from django.shortcuts import render
from empleado.serializer import EmpleadoSerializer, EstadoEmpleadoSerializer, DevengadoSerializer, NovedadDeduccionesSerializer, NovedadDevengadoSerializer, DeduccionesSerializer, NominaSerializer, TipoContratoSerializer, ContratoSerializer, HorasExtrasSerializer
from . models import Empleado, EstadoEmpleado, Devengado, Nomina, NovedadDeducciones,NovedadDevengado, Deducciones, TipoContrato, Contrato, HorasExtras
from rest_framework import viewsets

# Create your views here.
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset=Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EstadoEmpleadoViewSet(viewsets.ModelViewSet):
    queryset=EstadoEmpleado.objects.all()
    serializer_class = EstadoEmpleadoSerializer
    
class DevengadoViewSet(viewsets.ModelViewSet):
    queryset=Devengado.objects.all()
    serializer_class = DevengadoSerializer
    

class NovedaDevengadoViewSet(viewsets.ModelViewSet):
    queryset=NovedadDevengado.objects.all()
    serializer_class = NovedadDevengadoSerializer
    
class DeduccionesViewSet(viewsets.ModelViewSet):
    queryset=Deducciones.objects.all()
    serializer_class = DeduccionesSerializer
    
class NovedadDeduccionesViewSet(viewsets.ModelViewSet):
    queryset=NovedadDeducciones.objects.all()
    serializer_class = NovedadDeduccionesSerializer
    
class NominaViewSet(viewsets.ModelViewSet):
    queryset=Nomina.objects.all()
    serializer_class = NominaSerializer
    
class TipoContratoViewSet(viewsets.ModelViewSet):
    queryset=TipoContrato.objects.all()
    serializer_class = TipoContratoSerializer
    
class ContratoViewSet(viewsets.ModelViewSet):
    queryset=Contrato.objects.all()
    serializer_class = ContratoSerializer
    
class HorasExtrasViewSet(viewsets.ModelViewSet):
    queryset=HorasExtras.objects.all()
    serializer_class = HorasExtrasSerializer
    

