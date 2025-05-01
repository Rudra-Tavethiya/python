from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
    allstudents = student.objects.all()
    return render(request,"index.html",{"students":allstudents})

def register(request):
    
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        username = data.get("uname")
        email = data.get("email")
        phone = data.get("phone")
        age = data.get("age")

    
        if(id):
             stu = student.objects.get(pk=id)
             stu.username = username
             stu.email = email
             stu.phone = phone
             stu.age = age

             stu.save()

             return redirect("index")
        else:
            st = student.objects.create(username=username,email=email,phone=phone,age=age)

            if(st):
            # return render(request,'index.html',{'msg':"Registration successful"})
                return redirect("index")

    return render(request,"index.html")

def delete(request):
    stid = request.GET['stid']
    st = student.objects.get(pk=stid)
    st.delete()
    return redirect("index")

def update(request):
    stid = request.GET['stid']
    stu = student.objects.get(pk=stid)
    allstudents = student.objects.all()

    # return redirect("index")
    return render(request,"index.html",{"stu":stu,"students":allstudents})