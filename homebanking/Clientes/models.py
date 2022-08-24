
from django.db import models


# Create your models here.

class clientes(models.Model):
        name=models.TextField(max_length=40)
        surname=models.TextField(max_length=25)
        dni=models.IntegerField()
        direccion=models.TextField(max_length=100)
        tipo_cliente=models.TextField(max_length=30,default='tipo')