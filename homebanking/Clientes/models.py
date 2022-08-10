from django.db import models

# Create your models here.


class Project(models.Model):    #Hereda de Django para obtener funcionalidad que yo necesito
    tittle = models.CharField(max_length=200,verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)
    link =models.URLField(null=True,blank=True,verbose_name='Enlace Web')
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
    from django.db import models

class clientes(models.Model):
        customer_id=models.IntegerField()
        name=models.TextField(max_length=40)
        surname=models.TextField(max_length=25)
        dni=models.IntegerField()
        direccion=models.TextField(max_length=100)

class cuenta(models.Model):
        account_id=models.IntegerField()
        customer_id=models.IntegerField()
        balance=models.IntegerField()
        iban=models.TextField(max_length=100)
        tipo_de_cuenta_id=models.IntegerField()

class empleado(models.Model):
        employee_id=models.IntegerField()
        employee_name=models.TextField(max_length=100)
        employee_surname=models.TextField(max_length=100)
        employee_hire_date=models.TextField(max_length=300)
        employee_dni=models.TextField(max_length=100)
        branch_id=models.IntegerField()
        direccion_id=models.IntegerField()

class movimientos(models.Model):
        id_movimiento=models.IntegerField()
        iban=models.TextField(max_length=100)
        monto=models.IntegerField()
        tipo_operacion=models.TextField(max_length=200)
        hora=models.DateTimeField()

class prestamos(models.Model):
        loan_id=models.IntegerField()
        loan_type=models.TextField(max_length=200)
        loan_date=models.TextField(max_length=500)
        loan_total=models.IntegerField()
        customer_id=models.IntegerField()

class tarjetas(models.Model):
        tarjeta_id=models.IntegerField()
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