from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module')))

from module.features_xtrct import PhraseExtract
from module.token_tools import SpellingDetector
from module.token_tools import SpellCorrection
from module.ml_model import predict_level

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


#module for nlp pre-processes
from module.features_xtrct import PhraseExtract
from module.LanguageToolChecker import EssayExamineErrorSuggest

#model imports
from user.models import CustomUser, studentuser
from teacher.models import section, essay_assignment, context_question
from .models import essay_submitted, question_composition
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
@permission_classes([IsAuthenticated])
def studentInfo(req):
    #borrow the necessarry models from the user app to make this view process

    #validate the token, if valid get the user_id and query using the ORM, get the neccesarry information of the user using the user_id
    #if not valid return 401
    
    #print(access_token)

    try:

        access_token = req.GET.get('access')

        decoded_access_token = AccessToken(access_token)
        
        print(f"token_type: {decoded_access_token['token_type']}")
        print(f"exp: {decoded_access_token['exp']}")
        print(f"iat: {decoded_access_token['iat']}")
        print(f"jti: {decoded_access_token['jti']}")
        print(f"user_id: {decoded_access_token['user_id']}")


        user_id = int(decoded_access_token['user_id'])

        user = CustomUser.objects.get(id=user_id)

        #get the section using the id this student instance on the studentuser model

        user_studentinfo = studentuser.objects.get(user_id=user.id)


        return Response({
            "id" : decoded_access_token['user_id'],
            "username" : user.username,
            "section" : user_studentinfo.section
        })  

    except Exception as e:

        print(e)
        return Response({"message" : "invalid token"})

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def studentAssignments(req):

    #get the studentuser instance, then get the section
    #get the section instance, then get the section_key
    #get all the essay_assignment instance using the section_key

    try:
        
        acces_token = req.GET.get('access')

        decoded_access_token = AccessToken(acces_token)

        user_id = decoded_access_token['user_id']

        user =  studentuser.objects.get(user_id=user_id)

        section_instance = section.objects.get(section_code = user.section)

        assigmentQuerySet = essay_assignment.objects.filter(section_key=section_instance.id)

        assignment_list = [assignment.assignmentProperties() for assignment in assigmentQuerySet] 

        return Response({
            'message' : 'assignment list extracted',
            'assignments' : assignment_list
        }, status=status.HTTP_200_OK)

    except Exception as e:

        print(e)
    
    return


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def studentEssaySubmit(req):

    try:

        data = json.loads(req.body)

        
        essaycomposition = data.get('composition')
        assignment_id = data.get('assignment_id')

        decoded_access_token = AccessToken(data.get('access'))

        print('studentEssaySubmit in try block is executing')
        print(f"student user id : {decoded_access_token['user_id']}")
            

        #get the assignment_instance using the parameter assignment_id
        #create an assignment_submitted instance and set the assignment_code using the parameter assignment_instance.assignment_code
        #after creating the assignment_submitted instance, save it, then get the assignment_submitted.id, it will be a paramter for the question_essay intance

        assignment_instance = essay_assignment.objects.get(id=assignment_id)
        assignment_context_question = context_question.objects.filter(essay_assignment_key=assignment_instance.id)
        assignment_context_question_list = [question.getContext() for question in assignment_context_question]
        
        assignment_submit_instance = essay_submitted(student_id=decoded_access_token['user_id'], assignment_code=assignment_instance.assignment_code)
        assignment_submit_instance.save()

        for index, question in enumerate(assignment_context_question_list):

            quest_comp = question_composition(essay_submitted=assignment_submit_instance.id, question=question, composition=essaycomposition[index])
            quest_comp.save()




        #here implement the logic of sampleProcess from the user app -> sampleProcess() view

        question_para = quest_comp.question
        essay_composition_para = quest_comp.composition

        print(f"question_para : {question_para}")
        print(f"essay_composition_para {question_para}")


        #reinitialized variable for debugging
        question_para = 'What is your biggest fear?'
        essay_composition_para = 'The advancments in technolagy have revolutionized the way we comunicate and access information. With the rise of smartphons, tablets, and computers, people can now conect with others around the globe instanly. However, this rapid devlopment also comes with some challenges, such as the increase in cybercrime and the growing dependency on digital devices. As technolagy continues to evolve, it is crucial for societys to find a balance between embracing innovation and ensuring securty.'

        phrase_instance = PhraseExtract(question=question_para, text=essay_composition_para)


        # simulate the model prediction here
        
        Examine_result = [match.getDictPropeties() for match in EssayExamineErrorSuggest(PhraseInstance=phrase_instance)]
        # for each match.getDictProperties, make an instance of match
        # then balk_save 

        return Response({
            'message' : 'try block is executing',
            'assignment_details' : assignment_instance.assignmentProperties(),
            'assignment_submitted_id' : assignment_submit_instance.id, 
            'phrase_features' : phrase_instance.getFeatures(),
            'label' : predict_level(phrase_instance.getFeatures()),
            'suggestion' : Examine_result
            
        })

    except Exception as e:

        print(e)

        return 

    return

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def checkAssignmentDone(req):

    try:

        #using orm get the instance of essay_submitted using the parameters assignment_id and studentuser.user_id

        access_token = req.GET.get('access')
        assign_id = req.GET.get('assignment_id')

        decoded_access_token = AccessToken(access_token)

        essay_assignment_instance = essay_assignment.objects.get(id=assign_id)


        try:

            essay_submitted_instance = essay_submitted.objects.get(student_id=decoded_access_token['user_id'], assignment_code=essay_assignment_instance.assignment_code)

            return Response({
                'message' : f"Submitted",
                'found' : True
            }, status=status.HTTP_200_OK)

        except essay_submitted.DoesNotExist:

            
            return Response({
                'message' : f"Not Submitted",
                'found' : False
            }, status=status.HTTP_200_OK)
        

    except Exception as e:

        print(e)

        return