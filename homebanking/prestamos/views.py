from django.shortcuts import render,redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from prestamos.forms import PrestamosForm
from django.urls import reverse
from Clientes.models import prestamos as Prestamos
from datetime import date

# Create your views here.
@login_required
def prestamos(request):
    prestamo_form = PrestamosForm()
    projects = Project.objects.all()

    if request.method == 'POST':
        contact_form = PrestamosForm(data = request.POST)
        if prestamo_form.is_valid():
            monto_recibido = request.POST.get('monto','')
            meses_recibidos = request.POST.get('meses','')
            archivo_recibido = request.POST.get('archivo','')
        projectReceived = Project.object.get(pk=2)
        prestamo_recibido = Prestamos(loan_total = monto_recibido) #ACA TENGO QUE CREAR EL OBJETO PRESTAMO A CARGAR EN LA TABLA 
        #min 30 vidio clase
    return render(request,'prestamos/prestamos.html',{'projects':projects,'form': prestamo_form})


    
