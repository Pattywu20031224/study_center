from django.shortcuts import render
from django.views.generic import *
from .models import *
# Create your views here.

class Student(TemplateView):
    template_name= "Student/student.html"
    model=student
    
class StudentAdd(TemplateView):
    template_name="Student/student_add.html"

class StudentEdit(TemplateView):
    template_name="Student/student_edit.html"

