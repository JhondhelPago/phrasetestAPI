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
from . models import section, essay_assignment, context_question



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

            section_list.append(section_instance.propertiesToDict()) 

        return Response({
            'section_list' : section_list
        })
    
    except Exception as e:

        print(e) 
    
    return Response({'message' : 'invalid token'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def teacher_CreateEssayAssignment(req):

    try:

        data  = json.loads(req.body)

        decoded_access_token = AccessToken(data.get('access'))

        question_list = data.get('question_list')

        section_body  = data.get('section_body')    


        print(f"decoded_access_token: {decoded_access_token['user_id']}")
        print(f"question_list: {question_list}")
        print(f"section_body: {section_body}")
        print(section_body['id'])


        #used_id of the teacher
        user_id = int(decoded_access_token['user_id'])

        #check if the current section is associated with the teacher

        section_list = list(section.objects.filter(teacher_id=user_id))

        is_SectionBelongsToTeacher = False
        section_object = None

        for index, section_obj in enumerate(section_list):

            if section_body['section_code'] == section_obj.get_section_code():
                is_SectionBelongsToTeacher = True
                section_object = section_obj


            print(section_obj.get_section_id(), section_obj.get_section_code())


        # if belongs to the teacher
        if is_SectionBelongsToTeacher:
            #create an essay_assingment instance reference by section.id
            #if successfull then return a Response with status created

            assignment_instance = essay_assignment(section_key=section_object.id)
            print('assigning to essay_assingment is executing')
            assignment_instance.set_date_due(2024, 12, 21) 
            print(assignment_instance.date_due)
            #assingment_instance.time_created inside the model class

            #save the property of the instance
            assignment_instance.save()

            for context_q in question_list:

                context_question_instance = context_question(essay_assignment_key= assignment_instance.id, context=context_q)
                context_question_instance.save()

            #Reconstruct the Response with status created
            return Response({
                'essay_assignement_id' : assignment_instance.id,
                }, status=status.HTTP_201_CREATED)

    except Exception as e:

        print(e)

        return Response({'message' : F"exeception araise, {e}"})


 


