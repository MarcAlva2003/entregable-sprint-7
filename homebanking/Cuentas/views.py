from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Cuentas(request):
    projects = Project.objects.all()
    return render(request,'Cuentas/Cuentas.html', {'Cuentas': Cuentas})