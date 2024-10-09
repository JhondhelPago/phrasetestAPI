from features_xtrct import PhraseExtract
from token_tools import SpellingDetector



question = 'What is your biggest fear?'
essay = 'The advancments in technolagy have revolutionized the way we comunicate and access information. With the rise of smartphons, tablets, and computers, people can now conect with others around the globe instanly. However, this rapid devlopment also comes with some challenges, such as the increase in cybercrime and the growing dependency on digital devices. As technolagy continues to evolve, it is crucial for societys to find a balance between embracing innovation and ensuring securty.'


phraseInstance = PhraseExtract(question=question, text=essay)



print(phraseInstance.ArrayOfSents())


spellingDetect = SpellingDetector(phraseInstance.doc_sm)


for spellcorrection_obj in spellingDetect.correctionCollection:

    print(spellcorrection_obj)



