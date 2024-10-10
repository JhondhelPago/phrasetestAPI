import requests
import json

LanguageToolAPI = 'https://api.languagetool.org/v2/check'

def LangToolChecker(text):

    response = requests.post(LanguageToolAPI, 
        data={
            'text' : text,
            'language' : 'en-US',
        }
    )


    if response.status_code == 200:

        result = response.json()
        matches = result.get('matches', [])

        return matches
    
    else:
        print('Error post request to the langiage tool api')
        return "request did not satisfy. no feedback response."
    


#classes for structuring the response result of the LanguageToolAPI

# class ErrorSpotter:

#     def __init__(self, doc) -> None:
#         self.doc = 



