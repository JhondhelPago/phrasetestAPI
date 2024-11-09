import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from features_xtrct import PhraseExtract

Question1 = 'What do you want to be when you grow up? How will you get there?'
Question2  = 'What is the most valuable lesson you have learned in life?'

question = Question1
essay = 'When I grow up I\'d like to be a doctor of medicine. Doctors are very smart people and I want to be like them someday. I dreamed of treating the people sickness and cure them. I will study hard to attain my dreamed of becomeing a doctor. It may seem not easy but I will do best to one of them.'
essay1 = 'I love seafood  dishes. When we go home to our province, my grandmother serves as crab and lobster'
essay2 = 'In 20 years I imagined myself as a successful software engineer and a businessman. I dreamed to work as programmer at global tech companies like Google, Microsoft, and Apple. After 20 years, I also think that I already have agricultural businesses. During my age of 20s it is the time when i have to get married and start my own family, but before all of it I need to make sure that i have enough resources to support family\'s needs. I also want to explore my career opportunity overseas. I know that there a lot to discover on myself during my age of 20\'s and continue to improve my life quality.'

Phrase = PhraseExtract(question=question, text=essay2)


# Phrase.displayFeatures()
print(Phrase.getFeatures())
