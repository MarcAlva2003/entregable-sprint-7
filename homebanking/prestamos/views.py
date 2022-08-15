from django.shortcuts import render, redirect
from Clientes.models import clientes
from .models import Project
from .forms import LoanForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Clientes.models import prestamos as Prestamos
from datetime import datetime

# Create your views here.
@login_required
def prestamos(request):
    helper = clientes.objects.values('tipo_cliente')[0]
    user_client_type = 'classic'
    print(helper)
    loan_form = LoanForm()
    if request.method == "POST":
        loan_form = LoanForm(data=request.POST)
        
        if loan_form.is_valid():
            money_amount = int(request.POST.get('moneyAmount'))
            
            if (user_client_type == 'classic') and (money_amount > 100000):
                print('CLASSIC MAYOR')
                return redirect(reverse('prestamos') + "?amounterror")
            elif (user_client_type == 'gold') and (money_amount > 300000):
                print('GOLD MAYOR')
                return redirect(reverse('prestamos') + "?amounterror")
            elif money_amount > 500000:
                print('BLACK MAYOR')
                return redirect(reverse('prestamos') + "?errorblack")
            else:
                print('IF 2')
                return redirect(reverse('prestamos') + "?ok")

    projects = Project.objects.all() #Hay que hacer un .get filtrando por id de cliente y mostrar todos los prestamos
    #a la data que obtengo de aca hay que mostrarla en el content superior
    if loan_form.is_valid():
        money_amount = int(request.POST.get('moneyAmount'))
        monthsAmount_received = int(request.POST.get('monthsAmount'))
        loanType_received = int(request.POST.get('loanType'))
        prestamo = Prestamos(loan_approved_date=datetime.now(),loan_month = monthsAmount_received,loan_total=money_amount,loanType = loanType_received)
        prestamo.save()

    return render(request,'prestamos/prestamos.html', {'form':loan_form, 'client_type':user_client_type})

        # print(request.user.username)