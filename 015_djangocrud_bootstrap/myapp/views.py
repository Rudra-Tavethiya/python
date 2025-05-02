from django.shortcuts import render,redirect
from myapp.models import *

import os


# Create your views here.
def index(request):
    allstudents = student.objects.all()
    return render(request,"index.html", {"students":allstudents})

def register(request):
    if request.method == "POST":

        id = request.POST["id"]
        username = request.POST["uname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        age = request.POST["age"]
        image = request.FILES["img"]

        if id:
            stu = student.objects.get(pk=id)
            os.remove(stu.image.path)
            stu.username = username
            stu.email = email
            stu.phone = phone
            stu.age = age
            stu.image = image
            stu.save()

        else:
            
            student.objects.create(username=username, email=email, phone=phone, age=age, image=image)
        
        return redirect("index")



    return redirect("index")

def edit(request):
    sid = request.GET["sid"]
    edt = student.objects.get(pk=sid)
    allstudents = student.objects.all()
    return render(request,"index.html",{"students":allstudents , "edt":edt})


def delete(request):
    sid = request.GET["sid"]
    dlt = student.objects.get(pk=sid)
    os.remove(dlt.image.path)
    dlt.delete()
    return redirect("index")