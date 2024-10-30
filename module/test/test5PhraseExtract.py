import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from features_xtrct import PhraseExtract

Question1 = 'What do you want to be when you grow up? How will you get there?'
Question2  = 'What is the most valuable lesson you have learned in life?'

question = Question1
essay = 'When I grow up I\'d like to be a doctor of medicine. Doctors are very smart people and I want to be like them someday. I dreamed of treating the people sickness and cure them. I will study hard to attain my dreamed of becomeing a doctor. It may seem not easy but I will do best to one of them.'
essay1 = 'I love seafood  dishes. When we go home to our province, my grandmother serves as crab and lobster'

Phrase = PhraseExtract(question=question, text=essay)


Phrase.displayFeatures()
