from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class Homepage(TemplateView):
    template_name= "Homepage/home.html"