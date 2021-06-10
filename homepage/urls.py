from student.views import Student
from django.urls import *
from .views import *

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path('info/', Student.as_view(), name='student_info'),
]