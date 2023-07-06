from rest_framework import serializers
from .models import SchoolModel, SchoolClassModel, TeacherModel, StudentModel
from django.shortcuts import get_object_or_404

    
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = ('id', 'number','address','info')

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClassModel
        fields = ('id', 'name', 'capacity', 'school', 'info')
    
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ('id', 'name', 'lname', 'date_of_birth', 'photo', 'degree', 'salary', 'tclass', 'tschool', 'phone_number', 'email', 'address', 'password')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ('id', 'name', 'lname', 'grade', 'age', 'photo', 'date_of_birth', 'address', 'phone_number', 'email', 'steacher', 'sclass', 'sschool', 'password')

     
            