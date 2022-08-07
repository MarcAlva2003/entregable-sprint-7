from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request,'ITBANK/home.html')

def inversiones(request):

    return render(request,'ITBANK/inversiones.html')

def terminos(request):

    return render(request,'ITBANK/terminos.html')


def sucycajero(request):

    return render(request,'ITBANK/sucycajero.html')

def perfil(request):
    
    return render(request,'ITBANK/perfil.html')