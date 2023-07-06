from django.db import models
from datetime import datetime

# Create your models here.
class SchoolModel(models.Model):
    number = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    info = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.number
        
    
    class Meta:
        db_table = 'school_model'


class SchoolClassModel(models.Model):
    name = models.CharField(max_length=10)
    capacity = models.IntegerField(default=0)
    school = models.ForeignKey(SchoolModel, on_delete=models.SET_NULL, null=True)
    info = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'school_class_model'


class TeacherModel(models.Model):
    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    date_of_birth = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to="Teacher_photo/%Y/%m/%d", blank=True)
    degree = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    tclass = models.ForeignKey(SchoolClassModel, on_delete=models.SET_NULL, null=True)
    tschool = models.ForeignKey(SchoolModel, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    password = models.CharField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'teacher_model'
    


class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    grade = models.CharField(default='ordinary')
    age = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="Student_photo/%Y/%m/%d", blank=True)
    date_of_birth = models.DateField(default=datetime.now)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    steacher = models.ForeignKey(TeacherModel, on_delete=models.SET_NULL, null=True)
    sclass = models.ForeignKey(SchoolClassModel, on_delete=models.SET_NULL, null=True)
    sschool = models.ForeignKey(SchoolModel, on_delete=models.SET_NULL, null=True)
    password = models.CharField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'student_model'
