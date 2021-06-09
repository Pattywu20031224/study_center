from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class Teacher(TemplateView):
    template_name= "Teacher/teacher.html"

class TeacherView(TemplateView):
    template_name="Teacher/teacher_view.html"

class TeacherRollCall(TemplateView):
    template_name="Teacher/teacher_RollCall.html"