from django.contrib import admin
from . models import EstadoEmpleado, Empleado, Devengado, HorasExtras, NovedadDevengado, NovedadDeducciones, Deducciones, Nomina
# Register your models here.
admin.site.register(Empleado)
admin.site.register(EstadoEmpleado)
admin.site.register(Devengado)
admin.site.register(Deducciones)
admin.site.register(HorasExtras)
admin.site.register(NovedadDevengado)
admin.site.register(NovedadDeducciones)
admin.site.register(Nomina)