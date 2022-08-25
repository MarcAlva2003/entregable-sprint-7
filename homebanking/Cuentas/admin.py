from django.contrib import admin

# Register your models here.

from .models import cuenta

class CuentaAdmin (admin.ModelAdmin):
    pass
admin.site.register(cuenta)