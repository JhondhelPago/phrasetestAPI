from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import studentuser


# Create your models here.

class StudentUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = studentuser
        fields = ['id', 'email', 'firstname', 'middlename', 'lastname']
