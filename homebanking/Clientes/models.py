from django.db import models
# Create your models here.
class clientes(models.Model):
        name=models.TextField(max_length=40)
        surname=models.TextField(max_length=25)
        dni=models.IntegerField()
        direccion=models.TextField(max_length=100)
        tipo_cliente=models.TextField(max_length=30,default='tipo')
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        owner = models.ForeignKey('auth.User', related_name='clientes',on_delete=models.CASCADE)

class Meta:
        ordering = ("-created_at",)
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

def __str__(self):
        return self.nombre




