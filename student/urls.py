from django.urls import *
from .views import *

urlpatterns = [
    path("", Student.as_view(), name="student_add"),
    path("", Student.as_view(), name="student_edit")
]