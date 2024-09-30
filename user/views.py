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


# Create your views here.

#importing models
from .models import user, student_essay

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
def sample_para(req):

    if req.method  == 'GET':

        id_params = req.GET.get('param1', 'default_value1')

        data = {
            'id_origin' : id_params ,
            'message' : 'id received by the server'
        }


        found_user = user.objects.get(user_id=id_params)


        return JsonResponse(found_user.getJSON_Properties(), safe=False)
    

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
        spellingDetector = SpellingDetector(phrase_extract.text)
        print(spellingDetector.correctionCollection)


        
        

        return JsonResponse(
            {
                'POS_tags' : phrase_extract.POS_frequency(),
                'numberOfSentence' : phrase_extract.sentence_count(),
                'spelling_errors' : spellingDetector.correctionCollection
            }
        )

    return JsonResponse({'message' : 'method is not POST'})
        


    



