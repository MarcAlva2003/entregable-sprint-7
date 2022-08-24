from Clientes.models import clientes
from api.serializers import ClienteSerializer,UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from django.contrib.auth.models import User
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
        cliente = clientes.objects.all().order_by('created_at')
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClienteDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        cliente =clientes.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente)
        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


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