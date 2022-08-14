from django.db import models
from Clientes.models import Project

# Create your models here.

class PrestamoCliente(models.Model):    #Hereda de Django para obtener funcionalidad que yo necesito
    monto = models.FloatField(max_length=200,verbose_name="nombre")
    meses = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de pedido")
    prestamo = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.monto,self.meses,self.created