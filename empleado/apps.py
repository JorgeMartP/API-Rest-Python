from django.apps import AppConfig

class EmpleadoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'empleado'
    

class EmpleadoConfig(AppConfig):
    name = 'empleado'
    def ready(self):
        import empleado.signals 

