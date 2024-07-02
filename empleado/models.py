from django.db import models

# Create your models here.
class EstadoEmpleado(models.Model):
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.descripcion
    
class Empleado(models.Model):
    TIPO_DOCUMENT = (
        ("CC", "CC"),
        ("TI", "TI"),
        ("CE","CE"),
        ("CD","CD")
    )
    documento = models.CharField(max_length=15, primary_key=True)
    idEstado = models.ForeignKey(EstadoEmpleado, on_delete=models.CASCADE)
    tipoDocumento = models.CharField(choices=TIPO_DOCUMENT,  max_length=100)
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(default="")
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=250)
    departamento = models.CharField(max_length=250)
    salarioBasico = models.FloatField()
    def __str__(self):
        return self.nombre
    
class Devengado(models.Model):
    documento = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    totalDevengado = models.FloatField()
    periodo = models.DateField(blank=False)
    
    
class HorasExtras(models.Model):
    diurna = models.IntegerField()
    nocturna = models.IntegerField()
    diurnaDominical = models.IntegerField()
    nocturnaDominical = models.IntegerField()
    recargoDiurna = models.IntegerField()
    recargoNocturna = models.IntegerField()
    totalHoras = models.IntegerField()
    totalExtra = models.IntegerField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    codDevengado = models.ForeignKey(Devengado, on_delete=models.CASCADE)

class NovedadDevengado(models.Model):
    descripcion = models.CharField(max_length=200)
    total = models.FloatField()
    cantidad = models.IntegerField()
    codDevengado = models.ForeignKey(Devengado, on_delete=models.CASCADE)
    

class Deducciones(models.Model):
    documento = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    total = models.FloatField()
    periodo = models.DateField(blank=False)
    salud = models.FloatField()
    pension = models.FloatField()
    
class NovedadDeducciones(models.Model):
    descripcion = models.CharField(max_length=200)
    total = models.FloatField()
    cantidad = models.IntegerField()
    codDeducciones = models.ForeignKey(Deducciones, models.CASCADE)
    
class Nomina(models.Model):
    documento = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    codDeducciones = models.ForeignKey(Deducciones, on_delete=models.CASCADE)
    codDevengado = models.ForeignKey(Devengado, on_delete=models.CASCADE)
    total = models.FloatField()
    periodo = models.DateField(blank=False)
    
class TipoContrato(models.Model):
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.descripcion

class Contrato(models.Model):
    cargo = models.CharField(max_length=100)
    idTipoContrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    documento = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    salario = models.IntegerField()
    fechaInicio = models.DateField(blank=False)
    fechaFin = models.DateField(blank=False)
    jornadaLaboral = models.IntegerField()
    nivelRiesgo = models.CharField(max_length=100, null=True)