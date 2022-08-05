from django.shortcuts import render
from .models import Project

# Create your views here.

def Cuentas(request):
    projects = Project.objects.all()
    return render(request,'Cuentas/Cuentas.html')