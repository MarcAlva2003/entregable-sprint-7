from django.shortcuts import render, redirect
from Clientes.models import clientes
from .forms import LoanForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from prestamos.models import prestamos as Prestamos
from datetime import datetime

# Create your views here.

@login_required
def prestamos(request):

    prestamos_db = Prestamos.objects.filter(id_cliente__icontains = request.user.id)

    helper = clientes.objects.filter(id__icontains = request.user.id)
    user_client_type = helper[0].tipo_cliente
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
                money_amount = int(request.POST.get('moneyAmount'))
                monthsAmount_received = int(request.POST.get('monthsAmount'))
                loanType_received = request.POST.get('loanType')
                id_cliente_received = request.user.id
                prestamo = Prestamos(loan_approved_date=datetime.now(),loan_month = monthsAmount_received,loan_total=money_amount,loanType = loanType_received,id_cliente = id_cliente_received)
                prestamo.save()

    return render(request,'prestamos/prestamos.html', {'prestamos_db':prestamos_db,'form':loan_form, 'client_type':user_client_type})