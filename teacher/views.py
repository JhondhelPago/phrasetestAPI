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
from user.models import CustomUser, studentuser
from student.models import essay_submitted
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

        #1. using the section_code get the section_instance of it

        # section_body  = data.get('section_body') 
        section_code  = data.get('section_code')

        section_instance = section.objects.get(section_code=section_code)
    

        #used_id of the teacher
        user_id = int(decoded_access_token['user_id'])

        #check if the current section is associated with the teacher

        section_list = list(section.objects.filter(teacher_id=user_id))

        is_SectionBelongsToTeacher = False
        section_object = None

        for index, section_obj in enumerate(section_list):

            if section_instance.section_code == section_obj.get_section_code():
                is_SectionBelongsToTeacher = True
                section_object = section_obj
                break


            print(section_obj.get_section_id(), section_obj.get_section_code())


        # if belongs to the teacher
        if is_SectionBelongsToTeacher:
            #create an essay_assingment instance reference by section.id
            #if successfull then return a Response with status created

            #number of assignment correspond to its arragement, 
            current_ass_number = essay_assignment.objects.filter(section_key=section_object.id).count()

            assignment_instance = essay_assignment(section_key=section_object.id)
            assignment_instance.assignment_no = current_ass_number + 1
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





@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def section_details(req):

    try:

        section_code_params = req.GET.get('section_code')

        section_instance = section.objects.get(section_code=section_code_params)

        essay_assignment_QuerySet = essay_assignment.objects.filter(section_key=section_instance.id)

        # make a dictionary structure for the element if the QuerySet

        essay_assignment_info_list = [assignment.assignmentProperties() for assignment in essay_assignment_QuerySet]
                
        return Response({
            'section_id' : section_instance.id,
            'assignment_assoc' : essay_assignment_info_list
        })

    except Exception as e:

        print(e)
        return Response({
            'section_id' : None,
            'assignment_assoc' : None
        }, status=status.HTTP_406_NOT_ACCEPTABLE)   

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def essay_assignment_details(req):

    #extract necesarry information in this view block
    #the information will be display on the teacherpage based on the Current_Section State


    try:

        assignment_id = int(req.GET.get('assignment_id')) 
        

        assignment_instance = essay_assignment.objects.get(id=assignment_id)

        #Logic Here
        #1.Get the number of student, out of total student how many are them have done the assingment
        #Get the names of the student who have been submitted, name dateOfSubmission

        print(f"assignment_instance.section_key: {assignment_instance.section_key}")
        #1.
        
        #get the isntance of teh section using the section key of the assignment_instance
        section_instance = section.objects.get(id=assignment_instance.section_key)

        total_student = studentuser.objects.filter(section=section_instance.section_code).count() #filter() parameter should be section_code
        list_student_submitted = essay_submitted.objects.filter(assignment_code=assignment_instance.assignment_code)
        print(f"list_student_submitted: {list_student_submitted}")
        total_student_submitted = list_student_submitted.count()
        # print(f"total-student_submitted: {total_student_submitted}")


        #getting the context_question instance associated with this assignment
        context_question_instance = context_question.objects.get(essay_assignment_key=assignment_id)



        print(f"assignment_id : {assignment_id}")

        #get the names of the student who submitted tot this assingment
        #list of names
        #list of date_submitted
        # list of label
        

        #restructuring the Reponse body
        return Response({
            'message' : f"this is the assignment id : {assignment_id}",
            'assignment_details' : assignment_instance.assignmentProperties(),
            'student_total_in_section' : total_student,
            'total_student_submtted' : total_student_submitted,
            'submitted_student' : f"{total_student_submitted}/{total_student}",
            'context_question' : context_question_instance.getProperties()
            }, status=status.HTTP_200_OK)

    except Exception as e:

        print(e)

        return Response({
            "message": "assignment not found",
            "assignment_details": {
                "id": 0,
                "assignment_code": "",
                "assignment_no": "",
                "section_key": 0,
                "date_created": "",
                "date_due": ""
            },
            "student_total_in_section": "",
            "total_student_submtted": "",
            "submitted_student": "",
            "context_question" : context_question.getNoneProperties()
        }, status=status.HTTP_404_NOT_FOUND)


 


