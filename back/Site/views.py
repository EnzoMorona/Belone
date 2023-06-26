from rest_framework import viewsets
from Site.models import User, Post
from Site.serializer import UserSerializer, PostSerializer
from django.contrib.auth import authenticate, login
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        nome = request.data['nome']
        senha = request.data['senha']
        var = User.objects.filter(nome = nome).values_list('id')

    
        if (self.queryset.filter(nome = nome, senha = senha).first() is not None):
            return Response(status=status.HTTP_200_OK, data={var[0][0]})
        
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'erro':'Nome ou senha erradas'})
        
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

       
class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
        


    