from django.urls import *
from .views import *

urlpatterns = [
    path("rollcall", TeacherRollCall.as_view(), name="teacher_rollcall"),
    path("view", TeacherView.as_view(), name="teacher_view"),
]