from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import HorasExtras, Empleado, Contrato

@receiver(post_save, sender=HorasExtras)
def actualizar_total_extra(sender, instance, **kwargs):
    # Realiza aquí los cálculos para totalExtra
    total = (
        instance.diurna +
        instance.nocturna +
        instance.diurnaDominical +
        instance.nocturnaDominical +
        instance.recargoDiurna +
        instance.recargoNocturna
    )
    salario = instance.empleado.salarioBasico
    contrato = Contrato.objects.filter(documento=instance.empleado).order_by('-fechaInicio').first()
    jornadaLaboral = contrato.jornadaLaboral * 5
    valorhora = round(salario / jornadaLaboral)
    horaD = round((valorhora * 0.35) + valorhora)
    hExtraNocturna = round((valorhora * 0.75) + valorhora)
    hExtraDDominical = round((valorhora * 2) + valorhora)
    hExtraNDominical = round((valorhora * 2.5) + valorhora)
    hRecargoDominical = round((valorhora * 0.75) + valorhora)
    hRecargoNDominical = round((valorhora * 2.1) + valorhora)
    totalHoras = horaD + hExtraNocturna + hExtraNDominical + hExtraDDominical + hRecargoDominical + hRecargoNDominical
    # Actualiza el campo totalExtra
    instance.totalHoras = total
    instance.totalExtra = totalHoras
    instance.save()
    
