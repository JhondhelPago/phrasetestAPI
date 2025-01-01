from django.db import models
from django.utils import timezone
import string
import random
from datetime import date, datetime
import pytz

def dateforamatter(date, timezone='Asia/Manila'):

    tz = pytz.timezone(timezone)
    
    aware_date = date.astimezone(tz)

    formatted_date = aware_date.strftime("%B %d, %Y, %I:%M:%S %p")

    return formatted_date

class essay_submitted(models.Model):

    student_id = models.IntegerField()
    assignment_code = models.CharField(max_length=8, blank=True)
    date_submitted = timezone.now()

    def getDictProperties(self):

        return {
            'id' : self.id,
            'assignment_code' : self.assignment_code,
            'date_submitted' : self.date_submitted
        }
    
    def get_date_submitted(self):
    
        return dateforamatter(self.date_submitted)
    

    
class question_composition(models.Model):

    essay_submitted = models.IntegerField()
    question = models.CharField(max_length=500, blank=True)
    composition = models.CharField(max_length=16000, blank=True)
    comment = models.CharField(max_length=4000, default='')

    def getDictProperties(self):

        return {
            'id' : self.id,
            'essay_submitted' : self.essay_submitted,
            'question' : self.question,
            'composition' : self.composition,
            'comment' : self.comment
        }


class rubrics(models.Model):

    essay_submitted = models.IntegerField(blank=True, default=0)
    ideas = models.IntegerField(blank=True, default=0)
    gram_punc = models.IntegerField(blank=True, default=0)
    transition = models.IntegerField(blank=True, default=0)
    clarity = models.IntegerField(blank=True, default=0)
    word_choice = models.IntegerField(blank=True, default=0)
    structure = models.IntegerField(blank=True, default=0)
    lang_mechs = models.IntegerField(blank=True, default=0)
    label = models.CharField(max_length=30, blank=True, default='')

    def getBenchMarkScores(self):

        return {
            'ideas' : self.ideas,
            'gram_punc' : self.gram_punc,
            'transition' : self.transition,
            'clarity' : self.clarity,
            'word_choice' : self.word_choice,
            'structure' : self.structure,
            'lang_mechs' : self.lang_mechs,
            'label' : self.label
        }


class langtool_suggestion(models.Model):

    essay_submitted = models.IntegerField(blank=True, default=0)
    message = models.CharField(max_length=1500, blank=True, default='')
    shortmessage = models.CharField(max_length=1500, blank=True, default='')
    replacements = models.CharField(max_length=1500, blank=True, default='')
    context = models.CharField(max_length=1500, blank=True, default='')
    sentence = models.CharField(max_length=1500, blank=True, default='')
    final_sentence = models.CharField(max_length=1500, blank=True, default='')
    sentence_index = models.IntegerField(default=0)


    def getDictProperties(self):

        return {
            'id' : self.id,
            'message' : self.message,
            'shortmessage' : self.shortmessage,
            'replacements' : self.replacements,
            'context' : self.context,
            'sentence' : self.sentence,
            'final_sentence' : self.final_sentence,
            'essay_submitted' : self.essay_submitted,
            'sentence_index' : self.sentence_index
        }
    

class features(models.Model):

    essay_submitted = models.IntegerField(default=0)

    word_count = models.FloatField(default=0)
    unique_word_ratio = models.FloatField(default=0)
    average_word_length = models.FloatField(default=0)
    noun_count = models.FloatField(default=0)
    adj_count = models.FloatField(default=0)
    adv_count = models.FloatField(default=0)
    pronoun_count = models.FloatField(default=0)
    verb_count = models.FloatField(default=0)
    subordinating_clauses_count = models.FloatField(default=0)
    grammar_error_count = models.FloatField(default=0)
    spelling_error_count = models.FloatField(default=0)
    sentiment_polarity = models.FloatField(default=0)
    cohesive_device_count = models.FloatField(default=0)
    readability_score = models.FloatField(default=0)
    avg_sentence_length = models.FloatField(default=0)
    sentence_simple = models.FloatField(default=0)
    sentence_compound = models.FloatField(default=0)
    sentence_complex = models.FloatField(default=0)
    topic_relevance_score = models.FloatField(default=0)


    def getProperties(self):

        return {
            'word_count' : self.word_count,
            'unique_word_ratio' : self.unique_word_ratio,
            'average_word_length' : self.average_word_length,
            'noun_count' : self.noun_count,
            'adj_count' : self.adj_count,
            'adv_count' : self.adv_count,
            'pronoun_count' : self.pronoun_count,
            'verb_count' : self.verb_count,
            'subordinating_clauses_count' : self.subordinating_clauses_count,
            'grammar_error_count' : self.grammar_error_count,
            'spelling_error_count' : self.spelling_error_count,
            'sentiment_polarity' : self.sentiment_polarity,
            'cohesive_device_count' : self.cohesive_device_count,
            'readability_score' : self.readability_score,
            'avg_sentence_length' : self.avg_sentence_length,
            'sentence_simple' : self.sentence_simple,
            'sentence_compound' : self.sentence_compound,
            'sentence_complex' : self.sentence_complex,
            'topic_relevance_score' : self.topic_relevance_score
        }

class vocab_recom(models.Model):

    essay_submitted = models.IntegerField(default=0)    
    word = models.CharField(max_length=200, blank=True, default='')
    suggestion = models.CharField(max_length=500, blank=True, default='')


class context_understanding(models.Model):

    essay_submitted = models.IntegerField(default=0)
    sentence_number = models.IntegerField(default=0)
    sentence_orig = models.CharField(max_length=4000, blank=True, default='')
    messages = models.CharField(max_length=2000, blank=True, default=0)
    sentence_modif = models.CharField(max_length=4000, blank=True, default='')


    def getDictProperties(self):

        return {
            'essay_submitted' : self.essay_submitted,
            'sentece_number' : self.sentence_number,
            'sentence_orig' : self.sentence_orig,
            'messages' : self.messages.split('>'),
            'sentence_modif' : self.sentence_modif
        }
    
class error_summary(models.Model):

    essay_submitted = models.IntegerField(default=0)

    grammar = models.IntegerField(default=0)
    typos = models.IntegerField(default=0)
    typography = models.IntegerField(default=0)
    casing = models.IntegerField(default=0)
    punctuation = models.IntegerField(default=0)    
    spelling = models.IntegerField(default=0)
    style = models.IntegerField(default=0)
    redundancy = models.IntegerField(default=0)
    whitespace = models.IntegerField(default=0)
    misc = models.IntegerField(default=0)
    confused_words = models.IntegerField(default=0)
    contradiction = models.IntegerField(default=0)
    wordiness = models.IntegerField(default=0)
    date_time = models.IntegerField(default=0)
    names = models.IntegerField(default=0)
    numbers = models.IntegerField(default=0)
    inconsistency = models.IntegerField(default=0)
    passive_voice = models.IntegerField(default=0)
    missing_words = models.IntegerField(default=0)
    nonstandard_phrase = models.IntegerField(default=0)
    comma = models.IntegerField(default=0)
    colon_semicolon = models.IntegerField(default=0)