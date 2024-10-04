from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import StudentUserSerializer

#models
from user.models import studentuser



import json


# Create your views here.

@api_view(['POST'])
def login(req):

    data = json.loads(req.body)

    username = data.get('username')
    password = data.get('password')

    return Response({
        'your_username' : username,
        'your_password' : password
    })

@api_view(['POST'])
def signup(req):

    return Response({'message' : 'this is the signup views'})


@api_view(['GET'])
def getusers(req):

    studentusers = studentuser.objects.all()

    serializer = StudentUserSerializer(studentusers, many=True)

    # return Response({'message' : 'users loaded'})
    return Response(serializer.data)





