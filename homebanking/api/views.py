from urllib import response
from Clientes.models import clientes
from Cuentas.views import Cuentas
from api.serializers import ClienteSerializer,UserSerializer,SucursalSerializer,Sucursal
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from django.contrib.auth.models import User
from prestamos.models import prestamos as Prestamo
from prestamos.views import consultar, modificar,conectar,consultar
from Cuentas.models import cuenta as Cuenta
from .serializers import PrestamoSerializer, MontoPrestamosDeClienteSerializer
from tarjetas.models import Tarjetas
from tarjetas.serializer import TarjetaSerializer



# Create your views here.

class ClienteLists(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request): # nuevo
        
        permission_classes = [permissions.IsAuthenticated]
        if request.user.is_staff:
            cliente = clientes.objects.all().order_by('created_at')
            print(request.user.user_permissions.all())
            serializer = ClienteSerializer(cliente, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ClienteDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        if request.user.is_staff:
            cliente =clientes.objects.filter(pk=pk).first()
            
            serializer = ClienteSerializer(cliente)
            if cliente:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else: 
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
                


    def put(self, request, pk):
        print("Entrando a la actualizacion")
        cliente = clientes.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
#clase para manejar una única instancia
class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SucursalLists(APIView):
    def post(self, request, format=None):
        serializer = SucursalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request): # nuevo
        sucursales = Sucursal.objects.all().order_by('created_at')
        serializer = SucursalSerializer(sucursales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# una sucursal
class SucursalDetails(APIView):
    def get(self, request, pk):
        sucursal = Sucursal.objects.filter(pk=pk).first()
        serializer = SucursalSerializer(sucursal)
        if sucursal:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#una sucursal

class PrestamoList(APIView):
    
    def post(self, request, format=None):
        serializer = PrestamoSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def consultarSaldo(id):
#     conexion,cursor = conectar()
#     cursor.execute("SELECT id,account_id,balance,tipo_de_cuenta_id from Cuentas_cuenta")

#     for fila in cursor:
#         if fila[0] == id:
#             monto = fila[2]

#     conexion.close()

#     return monto


class PrestamoDetails(APIView):

    def delete(self,request, pk):
        #borra un prestamo con un id determinado
        prestamo = Prestamo.objects.filter(pk=pk).first()
        if prestamo:
            serializer = PrestamoSerializer(prestamo)
            
            prestamo = Prestamo.objects.get(pk = pk)
            cliente_id = prestamo.id_cliente
            cuenta = Cuenta.objects.get( account_id = cliente_id)
            monto_descuento = prestamo.loan_total
            monto_actual = cuenta.balance
            monto_actualizado = monto_actual - monto_descuento
            cuenta.balance = monto_actualizado
            cuenta.save()

            prestamo.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

# Tarjetas asociadas a un cliente

class TarjetasDeCliente(APIView):
    def get(self, request, customer_id):
        tarjeta = Tarjetas.objects.filter(customer_id=customer_id)
        serializer = TarjetaSerializer(tarjeta, many =  True)
        if tarjeta:
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)

# OBTENER MONTO DE PRESTAMOS DE UN CLIENTE
class MontoPrestamosDeCliente(APIView):
    def get(self, request, customer_id):
        prestamo = Prestamo.objects.filter(id_cliente=customer_id)
        serializer = MontoPrestamosDeClienteSerializer(prestamo, many= True)
        if prestamo:
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)