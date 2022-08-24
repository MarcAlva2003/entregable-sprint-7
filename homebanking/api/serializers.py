from rest_framework import serializers
from django.contrib.auth.models import User
from Clientes.models import clientes
from sucursales.models import Sucursal
from prestamos.models import prestamos as Prestamos

class ClienteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = clientes
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "owner",
        )

class UserSerializer(serializers.ModelSerializer):
    clientes = serializers.PrimaryKeyRelatedField(many=True, queryset=clientes.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'clientes']



class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura
        read_only_fields = (
        "id",
        "created_at",
        "updated_at",
        )

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Prestamos
        #indicamos que use todos los campos 
        fields = "__all__" 
        # #les decimos cuales son los de solo lectura 
        read_only_fields = ( 
            "id",
            "id_cliente",
            "created_at",
        )