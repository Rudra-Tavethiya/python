from django.urls import path
from doctor.views import *

urlpatterns = [
    path("",index,name="index")
]