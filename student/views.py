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
from module.features_xtrct import PhraseExtract, PhraseExtract1
from module.LanguageToolChecker import EssayExamineErrorSuggest
from module.rubrics import rubrics_benchmark, TransitionScore, WordChoiceScore, LanguageMechScore, StructureScore

#model imports
from user.models import CustomUser, studentuser
from teacher.models import section, essay_assignment, context_question
from .models import essay_submitted, question_composition, langtool_suggestion, rubrics, features

#imports from other apps

#import from student module
from student.module import get_unfinished_essay_assignment_id

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

# @csrf_exempt
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def studentAssignments(req):

#     #get the studentuser instance, then get the section
#     #get the section instance, then get the section_key
#     #get all the essay_assignment instance using the section_key

#     try:
        
#         acces_token = req.GET.get('access')

#         decoded_access_token = AccessToken(acces_token)

#         user_id = decoded_access_token['user_id']

#         user =  studentuser.objects.get(user_id=user_id)

#         section_instance = section.objects.get(section_code = user.section)

#         assigmentQuerySet = essay_assignment.objects.filter(section_key=section_instance.id)

#         assignment_list = [assignment.assignmentProperties() for assignment in assigmentQuerySet] 

#         return Response({
#             'message' : 'assignment list extracted',
#             'assignments' : assignment_list
#         }, status=status.HTTP_200_OK)

#     except Exception as e:

#         print(e)
    
#     return

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def studentAssignments(req):

    #parameter needed
    #acesstoken


    try:

        #get all of the id from essay_assignments in the student section

        #get all of the id from essay_submitted in the student section

        access_token = req.GET.get('access')
        decoded_access_token = AccessToken(access_token)
        user_id = decoded_access_token['user_id']

        user_instance = studentuser.objects.get(user_id=user_id)

        section_instance = section.objects.get(section_code=user_instance.section)

        essay_assignment_QuerySet = essay_assignment.objects.filter(section_key=section_instance.id)
        essay_assignment_id_list = [essay_assignment_instance.id for essay_assignment_instance in essay_assignment_QuerySet]
        essay_assignment_code_list = [essay_assignment_instance.assignment_code for essay_assignment_instance in essay_assignment_QuerySet]

        #instead of query from the essay_assignment, query from the essay_submitted
        FinishedAssignmentQuerySet = essay_submitted.objects.filter(student_id=user_instance.user_id, assignment_code__in=essay_assignment_code_list)
        FinishedAssignmentList_codes = [essay_submitted_instance.assignment_code for essay_submitted_instance in FinishedAssignmentQuerySet]


        assignmentQuerySet = essay_assignment.objects.filter(assignment_code__in=FinishedAssignmentList_codes)
        assignmentFinished_ids = [assignmentDone.id for assignmentDone in assignmentQuerySet]


        #only get the essay_assingment_id of un finished
        unfinished_ids = get_unfinished_essay_assignment_id(essay_assignment_id_list, assignmentFinished_ids)


        #filter to the queryset of essay_assignment_QuerySet
        #append only the instance with the matching id from unfinished_ids

        unfinished_assignmentObj_list = list()

        for id in unfinished_ids:

            for assignment in essay_assignment_QuerySet:

                if id == assignment.id:

                    unfinished_assignmentObj_list.append(assignment.assignmentProperties())

                    break



        return Response({
            'message' : 'assignment list extracted',
            'assignment_ids' : essay_assignment_id_list,
            'assingment_done_ids' : assignmentFinished_ids,
            'unfinished_assignment_id' : unfinished_ids,
            'assignments' : unfinished_assignmentObj_list
        })
    
    except Exception as e:

        return



@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def studentAssignmentFinished(req):

    #get the studentuser instance, then get the section
    #get the section instance, then get the section_key
    #get all the essay_assignment instance using the section_key

    try:

        access_token = req.GET.get('access')

        decoded_access_token = AccessToken(access_token)

        user_id = decoded_access_token['user_id']

        user_instance = studentuser.objects.get(user_id=user_id)

        section_instance = section.objects.get(section_code=user_instance.section)

        #all of the assignment in this student section
        essay_assignment_QuerySet = essay_assignment.objects.filter(section_key=section_instance.id)
        essay_assignment_id_list = [essay_assignment_instance.id for essay_assignment_instance in essay_assignment_QuerySet]
        essay_assignment_code_list = [essay_assignment_instance.assignment_code for essay_assignment_instance in essay_assignment_QuerySet]

        #instead of query from the essay_assignment, query from the essay_submitted
        FinishedAssignmentQuerySet = essay_submitted.objects.filter(student_id=user_instance.user_id, assignment_code__in=essay_assignment_code_list)
        FinishedAssignmentList_codes = [essay_submitted_instance.assignment_code for essay_submitted_instance in FinishedAssignmentQuerySet]


        assignmentQuerySet = essay_assignment.objects.filter(assignment_code__in=FinishedAssignmentList_codes)
        FinishedAssignmentList = [assignmentObj.assignmentProperties() for assignmentObj in assignmentQuerySet]


        #should return the a list of assignment id containing the 21, 23
        #should retunr empty list
        return Response({
            'message' : 'assingment list extracted.',
            'assignment_keys' : essay_assignment_id_list,
            'assignment_codes' : essay_assignment_code_list,
            'assignment_finished' : FinishedAssignmentList
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
        # question_para = 'What is your biggest fear?'
        # essay_composition_para = 'The advancments in technolagy have revolutionized the way we comunicate and access information. With the rise of smartphons, tablets, and computers, people can now conect with others around the globe instanly. However, this rapid devlopment also comes with some challenges, such as the increase in cybercrime and the growing dependency on digital devices. As technolagy continues to evolve, it is crucial for societys to find a balance between embracing innovation and ensuring securty.'

        phrase_instance = PhraseExtract1(question=question_para, text=essay_composition_para)


        # simulate the model prediction here

        #feature instance
        phrase_instance_features_dict = phrase_instance.getFeatures()
        
        print('Phase features')
        print(phrase_instance_features_dict)

        features_instance = features()
        features_instance.essay_submitted = assignment_submit_instance.id

        features_instance.word_count = phrase_instance_features_dict['word_count']
        features_instance.unique_word_ratio = phrase_instance_features_dict['unique_word_ratio']
        features_instance.average_word_length = phrase_instance_features_dict['average_word_length']
        features_instance.noun_count = phrase_instance_features_dict['noun_count']
        features_instance.adj_count = phrase_instance_features_dict['adj_count']
        features_instance.adv_count = phrase_instance_features_dict['adv_count']
        features_instance.pronoun_count = phrase_instance_features_dict['pronoun_count']
        features_instance.verb_count = phrase_instance_features_dict['verb_count']
        features_instance.subordinating_clauses_count = phrase_instance_features_dict['subordinating_clauses_count']
        features_instance.grammar_error_count = phrase_instance_features_dict['spelling_error_count']
        features_instance.sentiment_polarity = phrase_instance_features_dict['sentiment_polarity']
        features_instance.cohesive_device_count = phrase_instance_features_dict['cohesive_device_count']
        features_instance.readability_score = phrase_instance_features_dict['readability_score']
        features_instance.avg_sentence_length = phrase_instance_features_dict['avg_sentence_length']
        features_instance.sentence_simple = phrase_instance_features_dict['sentence_simple']
        features_instance.sentence_compound = phrase_instance_features_dict['sentence_compound']
        features_instance.sentence_complex = phrase_instance_features_dict['sentence_complex']
        features_instance.topic_relevance_score = phrase_instance_features_dict['topic_relevance_score']
        
        #saving the instance of features and inserting to the database
        features_instance.save()

        rubricsBenchmarkScores = rubrics_benchmark(phrase_instance)

        rubrics_instance = rubrics()
        rubrics_instance.essay_submitted = assignment_submit_instance.id
        # rubrics_instance.ideas = rubricsBenchmarkScores.Ideas_criterion
        rubrics_instance.ideas = features_instance.topic_relevance_score
        rubrics_instance.gram_punc = rubricsBenchmarkScores.Gram_Punc_criterion
        # rubrics_instance.transition = rubricsBenchmarkScores.Transition_criterion
        rubrics_instance.transition = TransitionScore(phrase_instance)
        rubrics_instance.clarity = rubricsBenchmarkScores.Clarity_criterion
        rubrics_instance.word_choice = WordChoiceScore(phrase_instance)
        rubrics_instance.structure = StructureScore(phrase_instance)
        rubrics_instance.lang_mechs = LanguageMechScore(phrase_instance)
        rubrics_instance.label = predict_level(phrase_instance.FeatureList1())

        rubrics_instance.save()

        try:

            Examine_result = [match.getImportantBody() for match in EssayExamineErrorSuggest(PhraseInstance=phrase_instance)]
            # for each match.getDictProperties, make an instance of match
            # then balk_save 

            #list of match object
            EssaySuggestionResult = list()

            for matchObj in Examine_result:

                match_parameters = matchObj

                langtool_suggestion_instance = langtool_suggestion()
                langtool_suggestion_instance.essay_submitted = assignment_submit_instance.id
                langtool_suggestion_instance.message = match_parameters['message']
                langtool_suggestion_instance.shortmessage = match_parameters['shortMessage']
                langtool_suggestion_instance.replacements = match_parameters['replacements']
                langtool_suggestion_instance.context = match_parameters['context']
                langtool_suggestion_instance.sentence = match_parameters['sentence']
                langtool_suggestion_instance.final_sentence = match_parameters['final_sentence']
                langtool_suggestion_instance.sentence_index = match_parameters['sentence_id']
                

                EssaySuggestionResult.append(langtool_suggestion_instance)

            langtool_suggestion.objects.bulk_create(EssaySuggestionResult)

        except Exception as e:

            print('EssayExamineErrorSuggestion function failed.')

            return Response({
                'message' : 'try block is executing',
                'assignment_details' : assignment_instance.assignmentProperties(),
                'assignment_submitted_id' : assignment_submit_instance.id, 
                'phrase_features' : phrase_instance.getFeatures(),
                'rubrics_benchmarks' : rubrics_instance.getBenchMarkScores(),
                'label' : rubrics_instance.label,
                'suggestion' : []
                
            })



        return Response({
            'message' : 'try block is executing',
            'assignment_details' : assignment_instance.assignmentProperties(),
            'assignment_submitted_id' : assignment_submit_instance.id, 
            'phrase_features' : phrase_instance.getFeatures(),
            'rubrics_benchmarks' : rubrics_instance.getBenchMarkScores(),
            'label' : rubrics_instance.label,
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
    
@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAssignmentResults(req):

    #parameter needed
    #assignment_id
    #student_id

    #get the instance of essay_submitted using the two parameter
    #store the id of the instance, the id value will be the reference key to the other models
    #make a structured reponse to return


    try:

        access_token  = req.GET.get('access')
        assignment_id = req.GET.get('assignment_id')

        decoded_access_token = AccessToken(access_token)

        student_id = decoded_access_token['user_id']


        #get the assignment_code here
        essay_assignment_instance = essay_assignment.objects.get(id=assignment_id)

        #essay_submitted_instance
        essay_submitted_instance = essay_submitted.objects.get(student_id=student_id, assignment_code=essay_assignment_instance.assignment_code)

        #usignthe essay_submitted_instance.id....
        #get the question_composition_instance
        #get the rubircs
        #get the langtool_suggestion

        question_composition_instance = question_composition.objects.get(essay_submitted=essay_submitted_instance.id)
        rubrics_instance = rubrics.objects.get(essay_submitted=essay_submitted_instance.id)
        features_instance = features.objects.get(essay_submitted=essay_submitted_instance.id)
        langtool_suggestion_instances = langtool_suggestion.objects.filter(essay_submitted=essay_submitted_instance.id)
        langtool_suggestion_list = [langtool_obj.getDictProperties() for langtool_obj in langtool_suggestion_instances]

        return Response({
            'message' : 'getAssignmentResults is executing',
            'student_id' : student_id,
            'assignment_id' : assignment_id,
            'essay_submitted_info' : essay_submitted_instance.getDictProperties(),
            'question_composition' : question_composition_instance.getDictProperties(),
            'rubrics' : rubrics_instance.getBenchMarkScores(),
            'features' : features_instance.getProperties(),
            'langtool_suggestion' : langtool_suggestion_list,
            
        }, status=status.HTTP_200_OK)

    except Exception as e:

        print(e)

        return Response({
            'error_message' : str(e)
        },status=status.HTTP_400_BAD_REQUEST)
    

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def JoinClass(req):

    try:

        data = json.loads(req.body)
        section_code_param = data.get('section_code')
        access = data.get('access')
        print(f"access:{access}")
        decoded_access_token = AccessToken(access)
        user_id = decoded_access_token['user_id']
        print(user_id)
        print(section_code_param)

        #validate first if the section_code exist
        #section_is_exist = section.objects.filter(section_code=section_code).exist
        #if the section_is_exist == True the proceed the process else return a Response with status that tells the section_code is invalid

        section_is_exist = section.objects.filter(section_code=section_code_param).exists()

        if not section_is_exist:
            print('section_is _exist control flow')
            return Response({
                'message' : f"'{section_code_param}' is invalid section code"
            }, status=status.HTTP_400_BAD_REQUEST)
    

        #get the studentuser instance using the user_id parameter to the getfunction of orm
        stud = studentuser.objects.get(user_id=user_id)
        stud.section = section_code_param
        stud.save()


        return Response({
            'message' : F"your id is {user_id}"
        }, status=status.HTTP_200_OK)
    
    except Exception as e:

        print(e)

        return Response({
            'message' : str(e)
        })