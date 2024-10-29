import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from LanguageToolChecker import SubStringInsertion, FindSubStringPosition, removeBothEndsDots


sentence = 'During my age of 20s it is the time when i have to get married and start my own family, but before all of it I need to make sure that i have enough resources to support family\'s needs.'

subsent = removeBothEndsDots('uring my age of 20s it is the time when i have to get married and start my own fa')


offset = FindSubStringPosition(SuperString=sentence, Substring=subsent)

print(f"offset index: {offset}")

result   = SubStringInsertion(original_string=sentence, start_index=offset, replacement_string='uring my age of 20s it is the time when I have to get married and start my own fa')

print(f"result: {result}")