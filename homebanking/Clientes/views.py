from django.shortcuts import render
from .models import Project

# Create your views here.

def Clientes(request):
    projects = Project.objects.all()
    return render(request,'Clientes/Clientes.html')