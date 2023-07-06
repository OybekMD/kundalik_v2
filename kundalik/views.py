from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import SchoolModel, SchoolClassModel, TeacherModel, StudentModel
from .serializers import SchoolSerializer, SchoolClassSerializer, TeacherSerializer, StudentSerializer


# ------------ School ------------
# GET, POST
class AllCreateSchoolView(generics.ListCreateAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer

# GET, DELETE
class DetailSchoolView(generics.RetrieveAPIView, generics.RetrieveDestroyAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer
    
# UPDATE -> patch, put
class UpdateSchoolView(generics.UpdateAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer


# ------------ SchoolClass ------------
# GET, POST
class AllCreateSchoolClassView(generics.ListCreateAPIView):
    queryset = SchoolClassModel.objects.all()
    serializer_class = SchoolClassSerializer

# GET, DELETE
class DetailSchoolClassView(generics.RetrieveAPIView, generics.RetrieveDestroyAPIView):
    queryset = SchoolClassModel.objects.all()
    serializer_class = SchoolClassSerializer

# UPDATE -> patch, put
class UpdateSchoolClassView(generics.UpdateAPIView):
    queryset = SchoolClassModel.objects.all()
    serializer_class = SchoolClassSerializer


# ------------ Teacher ------------
# GET, POST
class AllCreateTeacherView(generics.ListCreateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

# GET, DELETE
class DetailTeacherView(generics.RetrieveAPIView, generics.RetrieveDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

# UPDATE -> patch, put
class UpdateTeacherView(generics.UpdateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer


# ------------ Student ------------
# GET, POST
class AllCreateStudentView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

# GET, DELETE
class DetailStudentView(generics.RetrieveAPIView, generics.RetrieveDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

# UPDATE -> patch, put
class UpdateStudentView(generics.UpdateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer