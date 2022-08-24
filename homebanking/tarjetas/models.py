from tkinter import CASCADE
from django.db import models

# Create your models here.

class Project(models.Model):    #Hereda de Django para obtener funcionalidad que yo necesito
    tittle = models.CharField(max_length=200,verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)
    link =models.URLField(null=True,blank=True,verbose_name='Enlace Web')
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
    owner = models.ForeignKey('auth.user', related_name='posts', on_delete= models.CASCADE)

class tarjetas(models.Model):
        numero_tarjeta=models.IntegerField()
        cvv=models.IntegerField()
        fecha_emision=models.TextField(max_length=200)
        fecha_vencimiento=models.TextField(max_length=50)
        tipo_tarjeta_id=models.IntegerField()
        marca_tarjeta_id=models.IntegerField()
        account_id=models.IntegerField()


class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

def __str__(self) -> str:
        return self.tittle 