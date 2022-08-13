from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tarjetas(request):
    projects = Project.objects.all()
    return render(request,'tarjetas/tarjetas.html')