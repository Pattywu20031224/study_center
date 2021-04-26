from django.urls import *
from .views import *

urlpatterns = [
    path("", Homepage.as_view(), name="homepage")
]