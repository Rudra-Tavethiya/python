from django.urls import path
from myapp.views import *

urlpatterns = [
    path("getstudent",index,name="index"),
    path("addstudent",add,name="add"),
    path("update/<int:id>",update,name="update"),
    path("delete/<int:id>",delete,name="delete"),

    path("employees",getemp,name="employees"),
    path("employees/",addemp,name="employees/"),
    path("employees/<int:id>",updateemp,name="employees-update/"),
    path("employees/<int:id>/",deleteemp,name="employee-delete/"),

    path("product",productapi.as_view())

]
