from django.urls import *
from .views import *

urlpatterns = [
    path("", Teacher.as_view(), name="teacher_rollcall"),
    path("", Teacher.as_view(), name="teacher_view"),
]