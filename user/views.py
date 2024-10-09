from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


#module for nlp pre-processes
import  sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module')))

from module.features_xtrct import PhraseExtract
from module.token_tools import SpellingDetector
from module.token_tools import SpellCorrection

from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.Myserializer import StudentUserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from user.models import studentuser, CustomeUser


# Create your views here.

#importing models
from .models import student_essay

@api_view(['POST'])
def login(req):

    return Response({'mesage' : 'sample response from login view'})

@api_view(['POST'])
def signup(req):

    data = json.loads(req.body)
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    middle_name = data.get('middle_name')
    last_name = data.get('last_name')
    age = data.get('age')
    gender = data.get('gender')
    gradelevel = data.get('gradelevel')
    school_name = data.get('school_name')
    institutional_id = data.get('institutional_id')


    # checking the variable
    print(
        username,
        email,
        password,
        first_name,
        middle_name,
        last_name,
        gender,
        gradelevel,
        school_name,
        institutional_id

    )




    record_list = list(CustomeUser.objects.filter(email=email))

    if record_list:

        #make an error here or return message to the request


        data = {"message" : 'email is already taken by another user'}

        return Response(data, status=status.HTTP_204_NO_CONTENT)

    else:
        
        #make signup process here

        new_user = CustomeUser(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            age = age,
            gender = gender,
            school_name = school_name

        )

    
        #uploading the fields to the database on the table user_customeuser
        new_user.save()


        user_id = new_user.id

        AsStudentUser = studentuser(user_id=user_id, gradelevel=gradelevel, institutional_id=institutional_id)

        #upload the fields to the database on the table user_studentuser
        AsStudentUser.save()


        data = {

            "message" : "server is creating you as new user"
        }


        return Response(data, status=status.HTTP_201_CREATED)

    


    #check for existing email?
    # if not existing authenticate using otp
    






    # user = list(CustomeUser.objects.filter(email='jhondhelpago2307@gmail.com', password='1234'))
    
    # print(user[0].email)

    # return Response({'message' : f"sample response from signup view {user[0].email}"})


    return Response({'message' : first_name + ' ' + last_name})

@api_view(['GET'])
def token_test(req):

    return Response({'message' : 'sample response from token_test view'})
















def devs(req):

    data =  ['Chad', 'Ken', 'Solis', 'Pago']

    data = {
        'error' : ['typo', 'grammar'],
        'description' : [
            {
                'error type' : 'mali ka sa part na toh'
            },
            {
                'error type' : '6 years pare.'
            }
        ]
    }


    return JsonResponse(data, safe=False)
        

@csrf_exempt
def submitEssayInstance(req):

    if req.method == 'POST':
    
        data = json.loads(req.body)

        #using the data.get('string parameter') to access the property of the json object

        req_name = data.get('name')
        req_lastname = data.get('lastname')
        req_nickname = data.get('nickname')
        req_age = data.get('age')
        req_gender = data.get('gender')
        req_gradeLevel = data.get('gradeLevel')
        req_schoolFrom = data.get('schoolFrom')
        req_question1 = data.get('question1')
        req_answer1 = data.get('answer1')
        req_question2 = data.get('question2')
        req_answer2 = data.get('answer2')
        req_question3 = data.get('question3')
        req_answer3 = data.get('answer3')



        print(f"name: {req_name}")
        print(f"lastname: {req_lastname}")
        print(f"nickname: {req_nickname}")
        print(f"age: {req_age}")
        print(f"gender: {req_gender}")
        print(f"gradeLevel: {req_gradeLevel}")
        print(f"schoolFrom: {req_schoolFrom}")
        print(f"question1: {req_question1}")
        print(f"answer1: {req_answer1}")
        print(f"question2: {req_question2}")
        print(f"answer2: {req_answer2}")
        print(f"question3: {req_answer3}")
        print(f"question3: {req_question3}")



        #inserting to the MySQL database

        studentEssayInstance = student_essay(
            first_name = req_name,
            last_name = req_lastname,
            nick_name = req_nickname,
            age = req_age,
            # gender should have initiated here, syntax in this line ->  gender = req_gender
            gender = req_gender,
            grade_level = req_gradeLevel,
            school_from = req_schoolFrom,


            #essay fields
            question1 = req_question1,
            answer1 = req_answer1,

            question2 = req_question2,
            answer2 = req_answer2,

            question3 = req_question3,
            answer3 = req_answer3,

        )

        # #saving to the database
        studentEssayInstance.save()

        return JsonResponse({'message' : 'submitted to the database'})

    
    return JsonResponse({'message' : 'error to handle the \'submitEssayInstance\' views'})

@csrf_exempt
def sampleProcess(req):

    if req.method == 'POST':

        data = json.loads(req.body)


        question = data.get('question1')
        essaycomposition = data.get('composition')


        #use the mlp module here
        #convert the composition string into spacy doc object
        #instantiate the PhraseExtract
        #use the PhraseExtract to extract the phrases from the composition string
        #use the SpellCheck class to indentify the spelling error in the composition

        #--------------------------------------------------------------------------
        #return the result object of the processed compostion

        #print(essaycomposition)

        phrase_extract = PhraseExtract(question=question, text=essaycomposition)


        composition_result = {
            'word_count' : phrase_extract.wordCount(),
            'sentence_count' : phrase_extract.sentence_count(),

        }

        #SpellingDetector

        #instance of SpellingDetector
        print(phrase_extract.doc_sm)
        spellingDetector = SpellingDetector(phrase_extract.doc_sm)
        print(spellingDetector.correctionCollection)
        print(phrase_extract.ArrayOfSents())


        print('./')

        print(phrase_extract.cohesive_device_indentifier())

        
        

        return JsonResponse(
            {
                'Original_Composition' : phrase_extract.ArrayOfSents(),
                'POS_tags' : phrase_extract.POS_frequency(),
                'numberOfSentence' : phrase_extract.sentence_count(),
                'spelling_errors' : spellingDetector.correctionCollection
            }
        )

    return JsonResponse({'message' : 'method is not POST'})
        


    



