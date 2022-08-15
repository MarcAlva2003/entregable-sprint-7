from django.shortcuts import render, redirect
from Clientes.models import clientes
from .models import Project
from .forms import LoanForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def prestamos(request):
    helper = clientes.objects.filter(id__icontains = request.user.id)
    user_client_type = helper[0].tipo_cliente
    print(helper[0].tipo_cliente)
    loan_form = LoanForm()
    if request.method == "POST":
        loan_form = LoanForm(data=request.POST)
        
        if loan_form.is_valid():
            money_amount = int(request.POST.get('moneyAmount'))
            print()
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

    projects = Project.objects.all()
    return render(request,'prestamos/prestamos.html', {'form':loan_form, 'client_type':user_client_type })

        # print(request.user.username)