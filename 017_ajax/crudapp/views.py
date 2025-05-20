from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from crudapp.models import *


# Create your views here.
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method=="POST":
        uname = request.POST['uname']
        email = request.POST['email']
        age = request.POST['age']

       
        student.objects.create(uname=uname, email=email, age=age)
        return HttpResponse("Registration Successful")
    
    else:
        return render(request, "home.html")
    
def loaddata(request):
    students = student.objects.all()
    return JsonResponse({"data":list(students.values())})

def deletedata(request):
    sid = request.GET['sid']
    students = student.objects.get(pk=sid)
    students.delete()
    return HttpResponse("student deleted !!!")

def databyid(request):
    sid = request.GET['sid']
    students = student.objects.filter(pk=sid)
    return JsonResponse({"data":list(students.values())})

def updatedata(request):
    if request.method=="POST":
        data = request.POST

        id = data.get("id")

        students = student.objects.get(pk=id)
        students.uname = data.get("uname")
        students.email = data.get("email")
        students.age = data.get("age")
        students.save()

        return HttpResponse("updated successfully !!!")
        
def searchdata(request):
    keyword = request.GET['value']
    filterdata = student.objects.filter(uname__startswith=keyword)
    return JsonResponse({'data':list(filterdata.values())})