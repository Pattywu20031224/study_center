from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class Student(TemplateView):
    template_name= "Student/student.html"
    