from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

#module for nlp pre-processes
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module')))

from module.features_xtrct import PhraseExtract

#libary tools, classes and methods
from urllib.parse import unquote
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework  import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer


#model imports
from user.models import CustomUser
from . models import section



#Create your views here

@csrf_exempt
@api_view(['GET'])
def teacher_api_test_run(req):

    param_value = unquote(req.GET.get('access'))
    print(param_value)
    print(param_value)

    return Response({'message' : 'teacher_api_test_run is executing.'})

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teacherInfo(req):

    access_token = req.GET.get('access')
    print(f"access_token : {access_token}")

    try:

        decoded_access_token = AccessToken(access_token)
        print(f"user_id: {decoded_access_token['user_id']}")

        user_id = int(decoded_access_token['user_id'])

        user = CustomUser.objects.get(id=user_id)


        return Response({'user_id' : user_id, 'username' : user.username})

    except Exception as e:

        print(e)

        return Response({'message' : 'invalid token'})
    


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def section_list_view(req):


    try:

        access_token = req.GET.get('access')

        decoded_access = AccessToken(access_token)

        user_id = decoded_access['user_id']

        section_QuerySet = section.objects.filter(teacher_id=user_id)
        
        section_list = list()

        for section_instance in section_QuerySet:

            section_list.append(section_instance.section_code) 

        return Response({
            'section_list' : section_list
        })
    
    except Exception as e:

        print(e) 
    
    return Response({'message' : 'invalid token'})

