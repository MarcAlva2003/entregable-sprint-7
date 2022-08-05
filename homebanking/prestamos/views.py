from django.shortcuts import render
from .models import Project

# Create your views here.

def prestamos(request):
    projects = Project.objects.all()
    return render(request,'prestamos/prestamos.html')
