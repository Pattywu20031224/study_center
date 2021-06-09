from django.urls import *
from .views import *

urlpatterns = [
    path("add", StudentAdd.as_view(), name="student_add"),
    path("edit", StudentEdit.as_view(), name="student_edit")
]