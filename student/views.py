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


#imports from other apps



# Create your views here.
@csrf_exempt
@api_view(['GET'])
def student_api_test_run(req):

    param_value = unquote(req.GET.get('email'))

    print(f"param_value : {param_value}")    

    return Response({'message the student_api_test_run is executing'})

@csrf_exempt
@api_view(['GET'])
def studentInfo(req):

    #validate the token, if valid get the user_id and query using the ORM, get the neccesarry information of the user using the user_id
    #if not valid return 401
    


    access_token = req.GET.get('access')
    #print(access_token)


    try:

        decoded_access_token = AccessToken(access_token)
        
        print(f"token_type: {decoded_access_token['token_type']}")
        print(f"exp: {decoded_access_token['exp']}")
        print(f"iat: {decoded_access_token['iat']}")
        print(f"jti: {decoded_access_token['jti']}")
        print(f"user_id: {decoded_access_token['user_id']}")


        return Response({"id" : decoded_access_token['user_id']})

    except Exception as e:


        return Response({"message" : "invalid token"})


    return Response({'message' : 'studentInfo  view is executing'})
