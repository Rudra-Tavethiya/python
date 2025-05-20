from django.urls import path
from myapp.views import *


urlpatterns = [
    path('',index, name='index'),
    path('reg',reg,name='reg'),
    path('register',register, name='register'),
    path('user_login',user_login, name='user_login'),
    path('home',home, name='home'),
    path('user_logout',user_logout, name='user_logout'),    
]