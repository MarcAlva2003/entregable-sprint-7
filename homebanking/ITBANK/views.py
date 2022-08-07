from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request,'ITBANK/home.html')

def inversiones(request):

    return render(request,'ITBANK/inversiones.html')