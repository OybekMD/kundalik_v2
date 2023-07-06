from django.urls import path
from .views import AllCreateSchoolView, DetailSchoolView
from .views import AllCreateSchoolClassView, DetailSchoolClassView
from .views import AllCreateTeacherView, DetailTeacherView
from .views import AllCreateStudentView, DetailStudentView

urlpatterns = [
    path('school', AllCreateSchoolView.as_view()),
    path('school/<int:pk>', DetailSchoolView.as_view()),

    path('class', AllCreateSchoolClassView.as_view()),
    path('class/<int:pk>', DetailSchoolClassView.as_view()),

    path('teacher', AllCreateTeacherView.as_view()),
    path('teacher/<int:pk>', DetailTeacherView.as_view()),

    path('student', AllCreateStudentView.as_view()),
    path('student/<int:student_id>', DetailStudentView.as_view()),
]