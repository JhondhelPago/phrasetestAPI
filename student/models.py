from django.db import models
import string
import random
from datetime import date, datetime



class essay_submitted(models.Model):

    student_id = models.IntegerField()
    assignment_code = models.CharField(max_length=8, blank=True)
    date_submitted = models.DateField(default=datetime.now())

    def getDictProperties(self):

        return {
            'id' : self.id,
            'assignment_code' : self.assignment_code,
            'date_submitted' : self.date_submitted
        }
    

    
class question_composition(models.Model):

    essay_submitted = models.IntegerField()
    question = models.CharField(max_length=500, blank=True)
    composition = models.CharField(max_length=5000, blank=True)

    def getDictProperties(self):

        return {
            'id' : self.id,
            'essay_submitted' : self.essay_submitted,
            'question' : self.question,
            'composition' : self.composition
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



