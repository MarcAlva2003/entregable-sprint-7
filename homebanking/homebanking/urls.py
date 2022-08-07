"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ITBANK import views as ITBANK_views
from Clientes import views as Cliente_views
from Cuentas import views as Cuentas_views
from login import views as login_views
from prestamos import views as prestamos_views
from tarjetas import views as tarjetas_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ITBANK_views.home,name = 'home'),
    path('clientes/',Cliente_views.Clientes, name = 'clientes'),
    path('cuentas/',Cuentas_views.Cuentas, name = 'cuentas'),
    path('login/',login_views.login, name = 'login'),
    path('prestamos/',prestamos_views.prestamos, name = 'prestamos'),
    path('tarjetas/',tarjetas_views.tarjetas, name = 'tarjetas'),
    path('inversiones/',ITBANK_views.inversiones, name = 'inversiones')
]
