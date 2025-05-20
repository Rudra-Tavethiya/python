from django.urls import path
from crudapp.views import *

urlpatterns = [
    path('', home, name="home"),
    path('register', register, name="register"),
    path('loaddata', loaddata, name="loaddata"),
    path('deletedata',deletedata,name="deletedata"),
    path('databyid',databyid,name="databyid"),
    path('updatedata',updatedata,name="updatedata"),
    path('searchdata',searchdata,name="searchdata"),

]
