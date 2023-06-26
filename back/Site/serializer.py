from rest_framework import serializers
from Site.models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','nome','senha')
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','titulo','desc','nome')
        