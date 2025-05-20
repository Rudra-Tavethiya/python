
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name="index"),
    path('login',login,name="login"),
    path('signup',signup,name="signup"),
    path('home',home,name="home"),
    path('register',register,name="register"),
    path('logout',logout,name="logout"),

    

]
