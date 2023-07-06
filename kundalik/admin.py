from django.contrib import admin
from .models import SchoolModel, SchoolClassModel, TeacherModel, StudentModel
# Register your models here.
admin.site.register(SchoolModel)
admin.site.register(SchoolClassModel)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)
