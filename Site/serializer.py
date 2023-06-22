from rest_framework import serializers
from Site.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','nome','email')