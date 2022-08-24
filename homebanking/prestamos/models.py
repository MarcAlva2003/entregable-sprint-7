from django.db import models
from django import forms
from django.utils import timezone
from asyncio.windows_events import NULL

# Create your models here.

class LoanForm(forms.Form):
    moneyAmount = forms.IntegerField(label='Cantidad de dinero a pedir', required=True)
    monthsAmount = forms.IntegerField(label='Plazo en meses a pagar', required=True)
    customerSalary = forms.IntegerField(label='Ingreso mensual total', required=True)
    LOAN_TYPE_CHOICES = (
        ('hipotecario', 'Hipotecario'),
        ('prendario', 'Prendario'),
        ('personales', 'Personales'),
        ('con garantia', 'Con garantia'),
        ('sin garantia', 'Sin garantia'),

    )
    loanType = forms.ChoiceField(label='Seleccione tipo de prestamo a solititar', choices=LOAN_TYPE_CHOICES)
    termsAndConds = forms.BooleanField(label='Terminos y condiciones', required=True)


class prestamos(models.Model):
        loan_approved_date=models.DateField(timezone.now())
        loan_month=models.IntegerField(default=1)
        loan_total=models.FloatField(default=0)
        loanType=models.TextField(max_length=40, default='Personales')
        id_cliente=models.IntegerField(default=NULL)