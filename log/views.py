from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class Log(TemplateView):
    template_name= "Log/log.html"