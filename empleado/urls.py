from django.urls import path, include
from . import views
from rest_framework import routers
from empleado import views

router = routers.DefaultRouter()
router.register(r'empleado', views.EmpleadoViewSet)
router.register(r'estadoempleado', views.EstadoEmpleadoViewSet)
router.register(r'devengado', views.DevengadoViewSet)
router.register(r'novedad_devengado', views.NovedaDevengadoViewSet)
router.register(r'deducciones', views.DeduccionesViewSet)
router.register(r'novedad_deducciones', views.NovedadDeduccionesViewSet)
router.register(r'nomina', views.NominaViewSet)
router.register(r'contrato', views.ContratoViewSet)
router.register(r'tipo_contrato', views.TipoContratoViewSet)
router.register(r'horasextra', views.HorasExtrasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]