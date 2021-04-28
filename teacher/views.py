from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class Teacher(TemplateView):
    template_name= "Teacher/teacher.html"