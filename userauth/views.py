from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json


# Create your views here.

@api_view(['POST'])
def login(request):

    data = json.loads(request.body)

    username = data.get('username')
    password = data.get('password')

    return Response({
        'your_username' : username,
        'your_password' : password
    })



