from django.shortcuts import render
from .models import Project

# Create your views here.

def tarjetas(request):
    projects = Project.objects.all()
    return render(request,'tarjetas/tarjetas.html')