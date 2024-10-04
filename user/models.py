from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class studentuser(models.Model):

    class Meta:

        db_table = 'studentuser'

        ordering = [
            'id',
            'email',
            'firstname',
            'middlename',
            'lastname',
            'age',
            'gender',
            'gradelevel',
            'schoolname',
            'school_id'
        ]


    #choice list for gender
    gender_choice = [
        ('M', 'male'),
        ('F', 'female')
    ]

    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=80)
    username = models.CharField(max_length=250)
    firstname = models.CharField(max_length=80)
    middlename = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gender_choice)
    gradelevel = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    schoolname = models.CharField(max_length=250)
    school_id = models.CharField(max_length=20)



    def display_info(self):

        return f"user_id: {self.user_id}, username: {self.username}"
    
    def getJSON_Properties(self):

        return {
            "user_id": self.user_id,
            "username": self.username
        }
    
    
class student_essay(models.Model):

    student_instance_id = models.AutoField(primary_key=True)
    first_name = models.TextField(default='None')
    last_name = models.TextField(default='')
    nick_name = models.TextField(default='')
    age = models.IntegerField(default='')
    gender = models.TextField(default='')
    grade_level = models.IntegerField(default=6)
    school_from = models.TextField(default='')
    

    #essay fields
    question1 = models.TextField(default='')
    answer1 = models.TextField(default='')

    question2 = models.TextField(default='')
    answer2 = models.TextField(default='')

    question3 = models.TextField(default='')
    answer3 = models.TextField(default='')


    class Meta:

        db_table = 'student_essay'
        ordering = [
            'student_instance_id',
            'first_name',
            'last_name',
            'nick_name',
            'age',
            'gender',
            'grade_level',
            'school_from',

            'question1',
            'answer1',
            'question2',
            'answer2',
            'question3',
            'answer3'
        ]



    def display_information(self):

        print(f"student_instance_id: {self.student_instance_id}")
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"nick_name: {self.nick_name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"grade_level: {self.grade_level}")
        print(f"school_from: {self.school_from}")


     
