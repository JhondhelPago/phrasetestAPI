from user.models import CustomeUser 
from rest_framework import serializers


class StudentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomeUser
        fields = ('id', 'username', 'email', 'password')


    