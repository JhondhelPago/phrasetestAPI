from django.db import models
import string
import random
from datetime import date

# Create your models here.


def generate_section_code():

    length = 8
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

def generate_assignment_code():

    return generate_section_code()

class section(models.Model):

    section_name = models.CharField(max_length=50, null=True)
    section_code = models.CharField(max_length=8, unique=True, blank=True)
    teacher_id = models.IntegerField(null=True)
    


    def propertiesToDict(self):

        return {
            'id' : self.id,
            'section_code' : self.section_code,
            'section_name' : self.section_name
        }
    
    def get_section_id(self):

        return self.id

    def get_section_code(self):

        return self.section_code
    

    def save(self, *args, **kwargs):

        if not self.section_code:

            self.section_code = generate_section_code()

            while section.objects.filter(section_code=self.section_code).exists():
                self.section_code = generate_section_code()

            super(section, self).save(*args, **kwargs)


class essay_assignment(models.Model):

    assignment_code = models.CharField(max_length=8, unique=True, blank=True)
    section_key = models.IntegerField(blank=True)
    context = models.CharField(max_length=500, blank=False)
    due_date = models.DateField(blank=True, null=True) #parameter format -> due_date=date(2024, 11, 15) -> date(YYYY, MM, DD), import the date object.


    def set_due_date(self, YYYY, MM, DD):

        self.due_date = date(YYYY, MM, DD)


    def save(self, *args, **kwargs):


        if not self.assignment_code:

            self.assignment_code = generate_assignment_code()

            while essay_assignment.objects.filter(assignment_code=self.assignment_code).exists():

                self.assignment_code = generate_assignment_code()

            super(essay_assignment, self).save(*args, **kwargs)

    



