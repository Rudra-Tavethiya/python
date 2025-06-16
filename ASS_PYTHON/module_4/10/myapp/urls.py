from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",login,name="login"),
    path("signup",signup,name="signup"),
    path("home",home,name="home"),
    path("adduser",adduser,name="adduser")
]