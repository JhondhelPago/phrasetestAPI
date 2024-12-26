import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


#import the PhraseExtract class
#import the Vocabulary class


from new_features_xtract import PhraseExtract
from app_feature import Vocabulary, synonyms, get_synonyms, underscoreTospace, sort_synonyms


context = """Phones and driving"""
essay_text = """ Phones

Modern humans today are always on their phone. They are always on their phone more than 5 hours a day no stop .All they do is text back and forward and just have group Chats on social media. They even do it while driving. They are some really bad consequences when stuff happens when it comes to a phone. Some certain areas in the United States ban phones from class rooms just because of it.

When people have phones, they know about certain apps that they have .Apps like Facebook Twitter Instagram and Snapchat. So like if a friend moves away and you want to be in contact you can still be in contact by posting videos or text messages. People always have different ways how to communicate with a phone. Phones have changed due to our generation.

Driving is one of the way how to get around. People always be on their phones while doing it. Which can cause serious Problems. That's why there's a thing that's called no texting while driving. That's a really important thing to remember. Some people still do it because they think It's stupid. No matter what they do they still have to obey it because that's the only way how did he save.

Sometimes on the news there is either an accident or a suicide. It might involve someone not looking where they're going or tweet that someone sent. It either injury or death. If a mysterious number says I'm going to kill you and they know where you live but you don't know the person's contact ,It makes you puzzled and make you start to freak out. Which can end up really badly.

Phones are fine to use and it's also the best way to come over help. If you go through a problem and you can't find help you ,always have a phone there with you. Even though phones are used almost every day as long as you're safe it would come into use if you get into trouble. Make sure you do not be like this phone while you're in the middle of driving. The news always updated when people do something stupid around that involves their phones. The safest way is the best way to stay safe.    """


# print(f"context: {context}")
# print(f"text: {essay_text}")


Phrase = PhraseExtract(question=context, text=essay_text)

Vocab = Vocabulary(Phrase=Phrase)

#print(Vocab.wordList)
# print(Vocab.word_freq_pair)
print(Vocab.repeated_word) # array of tuples arrange by the frequency of the words



print('Synonyms testing: \n')

test_word = 'phone'

print(f"word : {test_word}")

print('synonyms suggestion:')

alternative_words = get_synonyms(test_word)
print(alternative_words)

print('\n')
print('sematic relationship word by word')

atlternative_words_relevance = sort_synonyms(test_word, alternative_words)

print(atlternative_words_relevance)


print('\n')
print('final words to make a vocabulary recommendation')
print(Vocab.Vocab_Recom())
 



