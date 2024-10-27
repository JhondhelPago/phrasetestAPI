from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, get_user_model
import json


#module for nlp pre-processes
import  sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module')))


from module.features_xtrct import PhraseExtract
from module.token_tools import SpellingDetector
from module.token_tools import SpellCorrection
from module.dummy_module_dir.module1 import greet

from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.Myserializer import StudentUserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer
from user.models import teacheruser,studentuser, CustomUser, UserOTP

from user.user_mail import send_mail

#function and classe from the user_module
from datetime import datetime, timezone
from user.user_module import otp_generator, time_dissect, time_difference, time_dif_under2mins, removeUTC_symbol



# Create your views here.

#importing models
from .models import student_essay







@csrf_exempt
@api_view(['POST'])
def login(req):

    data = json.loads(req.body)

    email = data.get('email')
    password = data.get('password')


    # user = authenticate(req, email=email, password=password)

    # if user is not None:


    #     refresh = RefreshToken.for_user(user)


    #     return Response({
    #         "refresh" : str(refresh),
    #         "access" : str(refresh.access_token)
    #     })
    


    UserModel = get_user_model()

    try: 
        user = UserModel.objects.get(email=email, password=password, verified=1)


        if user is not None:


            refresh = RefreshToken.for_user(user)


            return Response({
                "user_type" : 'student' if user.is_student else 'teacher',
                "token" : {"refresh" : str(refresh), "access" : str(refresh.access_token)}
            }, status=status.HTTP_200_OK)
        
    except CustomUser.DoesNotExist:

        return Response({
            "user_type" : None,
            "token" : {"refresh" : "", "access" : ""}
        }, status=status.HTTP_404_NOT_FOUND)
    
@csrf_exempt
@api_view(['POST'])
def signup_student(req):

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




    record_list = list(CustomUser.objects.filter(email=email))

    if record_list:

        #make an error here or return message to the request


        #data = {"email_exist" : True}

        #return Response(data, status=status.HTTP_204_NO_CONTENT)

        if record_list[0].verified == True:

            data = {"email_exist" : True}

            return Response(data, status=status.HTTP_204_NO_CONTENT)

        else:
            print('dito ang control flow')
            # delete the instance on the userotp, studentuser and customuser
        
            user_id = record_list[0].id

            UserOTPInstance = UserOTP.objects.get(user_id=user_id)
            UserOTPInstance.delete()

            StudentUserInstance = studentuser.objects.get(user_id=user_id)
            StudentUserInstance.delete()
            
            record_list[0].delete()
            
    record_list = list(CustomUser.objects.filter(email=email))

    if not record_list:
        
        #make signup process here

        new_user = CustomUser(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            age = age,
            gender = gender,
            is_student = True,
            school_name = school_name

        )

    
        #uploading the fields to the database on the table user_customeuser
        new_user.save()


        user_id = new_user.id

        AsStudentUser = studentuser(user_id=user_id, gradelevel=gradelevel, institutional_id=institutional_id)
        #upload the fields to the database on the table user_studentuser
        AsStudentUser.save()


        #make an instance of userotp here
        userotp = UserOTP(user_id=user_id)
        userotp.otp = otp_generator()
        
        #save the otp 
        userotp.save()


        #send an email to provided email address and deliver the otp code
        content_body = f"signup otp code {userotp.otp} for phrasetest app."
        send_mail(email, content_body)

        data = {

            "email_exist" : False,
            "message" : "signup successfully verified."
        }


        return Response(data, status=status.HTTP_201_CREATED)
    
@csrf_exempt
@api_view(['POST'])
def signup_teacher(req):

    data = json.loads(req.body)
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    middle_name = data.get('middle_name')
    last_name = data.get('last_name')
    age = data.get('age')
    gender = data.get('gender')
    school_name = data.get('school_name')



    record_list = list(CustomUser.objects.filter(email=email))

    if record_list:

        #make an error here or return message to the request

        #data = {"email_exist" : True}

        #return Response(data, status=status.HTTP_204_NO_CONTENT)

        if record_list[0].verified == True:

            data = {"email_exist" : True}

            return Response(data, status=status.HTTP_204_NO_CONTENT)

        else:
            print('dito ang control flow')
            # delete the instance on the userotp, studentuser and customuser
        
            user_id = record_list[0].id

            UserOTPInstance = UserOTP.objects.get(user_id=user_id)
            UserOTPInstance.delete()

            TeacherUserInstance = teacheruser.objects.get(user_id=user_id)
            TeacherUserInstance.delete()
            
            record_list[0].delete()
            
    record_list = list(CustomUser.objects.filter(email=email))

    if not record_list:
        
        #make signup process here

        new_user = CustomUser(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            age = age,
            gender = gender,
            is_teacher = True,
            school_name = school_name

        )

    
        #uploading the fields to the database on the table user_customeuser
        new_user.save()


        user_id = new_user.id

        AsTeacherUser = teacheruser(user_id=user_id)
        #upload the fields to the database on the table user_studentuser
        AsTeacherUser.save()


        #make an instance of userotp here
        userotp = UserOTP(user_id=user_id)
        userotp.otp = otp_generator()
        
        #save the otp 
        userotp.save()


        #send an email to provided email address and deliver the otp code
        content_body = f"signup otp code {userotp.otp} for phrasetest app."
        send_mail(email, content_body)

        data = {

            "email_exist" : False,
            "message" : "signup successfully verified."
        }


        return Response(data, status=status.HTTP_201_CREATED)

    


    #check for existing email?
    # if not existing authenticate using otp
    

    # user = list(CustomeUser.objects.filter(email='jhondhelpago2307@gmail.com', password='1234'))
    
    # print(user[0].email)

    # return Response({'message' : f"sample response from signup view {user[0].email}"})
@csrf_exempt
@api_view(['GET'])
def token_test(req):

    return Response({'message' : 'sample response from token_test view'})

@csrf_exempt
@api_view(['POST'])
def new_accesstoken(req):

    data = json.loads(req.body)

    refresh_token = data.get('refresh')
    access_token = data.get('access')

    try:

        decoded_refresh_token = RefreshToken(refresh_token)

        print(f"token_type: {decoded_refresh_token['token_type']}")
        print(f"exp: {decoded_refresh_token['exp']}")
        print(f"iat: {decoded_refresh_token['iat']}")
        print(f"jti: {decoded_refresh_token['jti']}")
        print(f"user_id: {decoded_refresh_token['user_id']}")



        decoded_access_token = AccessToken(access_token)
        
        print(f"token_type: {decoded_access_token['token_type']}")
        print(f"exp: {decoded_access_token['exp']}")
        print(f"iat: {decoded_access_token['iat']}")
        print(f"jti: {decoded_access_token['jti']}")
        print(f"user_id: {decoded_access_token['user_id']}")


        return Response({"id" : decoded_refresh_token['user_id']})

    except Exception as e:


        return Response({"message" : "invalid token"})
    
@csrf_exempt
@api_view(['POST'])
def otp_verify(req):

    #get the id of the user using the email parameter
    #find the generated otp of the user and get created_at
    #created_at is time_dif_under2mins() parameter1
    #request_time is time_dif_under2mins() parameter2
    #if under 2mins validate the otp, if validated verify the user using the orm 

    data = json.loads(req.body)
    print(data)

    req_otp_code = data.get('otp_code')

    request_time = data.get('time_created')
    print(f"request_time: {request_time}")
   

    try:

        user_instance = CustomUser.objects.get(email=data.get('email'))
        print(user_instance)
        
        user_id = user_instance.id

        user_opt_instance = UserOTP.objects.get(user_id=user_id)
        
        generated_Otp = user_opt_instance.otp

        otp_created_at = removeUTC_symbol(user_opt_instance.created_at)
        print(f"otp_created_at: {otp_created_at}")
        

    except CustomUser.DoesNotExist:

        return Response({
            "message" : "email not found", "result" : -1
        }, status=status.HTTP_404_NOT_FOUND)
    
    if time_dif_under2mins(otp_created_at, request_time):

        print(f"True: {time_dif_under2mins(otp_created_at, request_time)}")

        if req_otp_code == generated_Otp:

            user_opt_instance.is_verified = True
            user_opt_instance.save()

            user_instance.verified = True
            user_instance.save()

            send_mail(data.get('email'), body='Welcome to Phrasetest! Login to PhaseTest and explore.', Subject='Account Verified')

            return Response({"message" : "user validated", "result" : 1}, status=status.HTTP_202_ACCEPTED)

    else:
        print(f"False: {time_dif_under2mins(otp_created_at, request_time)}")

        return Response({"message" : "otp expires", "result" : 0}, status=status.HTTP_408_REQUEST_TIMEOUT)
    


    return Response({"message" : "otp_verify view  is runnung."}, status=status.HTTP_102_PROCESSING)


@csrf_exempt
@api_view(['POST'])
def otp_reverify(req):

    data = json.loads(req.body)

    email = data.get("email")

    try:

        user = CustomUser.objects.get(email=email)

    except CustomUser.DoesNotExist:

        user = None


    if user == None:

        return Response({"message" : f"{email} is not yet registered to sign up"}, status=status.HTTP_404_NOT_FOUND)
    
    else:

        if user.verified:

            return Response({"message" : "email is already verified user"}, status=status.HTTP_403_FORBIDDEN)
        
        else:

            print(user)
            print(user.id)

            user_id = user.id

            user_otp_instance = UserOTP.objects.get(user_id=user_id)
            user_otp_instance.otp = otp_generator()
            user_otp_instance.created_at = datetime.now(timezone.utc)
            user_otp_instance.is_verified = False
            user_otp_instance.save()

            #send the new otp to the email here

            try:

                content_body = f"signup otp code {user_otp_instance.otp} for phrasetest app."
                send_mail(email, body=content_body, Subject='New Otp')

                return Response({"message" : "new otp generated"}, status=status.HTTP_200_OK)


            except Exception as e:

                print(e)

                return Response({"message" : "otp resend failed."}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message" : "otp_reverify running"})


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


@csrf_exempt
@api_view(['GET'])
def sample_view_get(req):

    try:

        email = req.GET.get('email')

        return Response({"message" : greet(email)})

    except Exception as e:

        return Response({"error" : str(e)})


        


class CustomTokenRefreshView(TokenRefreshView):

    serializer_class = TokenRefreshSerializer


    def post(self, request):


        return super().post(request)
    

class CustomeTokenObtainView(TokenObtainPairView):

    serializer_class = TokenObtainPairSerializer

    def post(self, request):

        return super().post(request)

