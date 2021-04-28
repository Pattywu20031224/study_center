from django.urls import *
from .views import *

urlpatterns = [
    path("", Student.as_view(), name="student")
]