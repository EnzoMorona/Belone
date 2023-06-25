from rest_framework import viewsets
from Site.models import User
from Site.serializer import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        user = request.data['nome']
        password = request.data['senha']
    
        if (self.queryset.filter(nome=user, senha=password).first() is not None):
            return Response(status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    