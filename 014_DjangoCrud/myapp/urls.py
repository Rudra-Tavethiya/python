
from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name='index'),
    path("register",register,name="register"),
    path("delete",delete,name="delete"),
    path("update",update,name="update"),
]
