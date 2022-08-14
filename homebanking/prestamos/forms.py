from django import forms

class PrestamosForm(forms.Form):

    monto = forms.FloatField(label='monto',required=True)
    meses = forms.IntegerField(label="meses", required=True)
    archivo = forms.FileField(label="archivo recibo de sueldo",required=False)
