from user.models import CustomUser 
from rest_framework import serializers


class StudentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')


    