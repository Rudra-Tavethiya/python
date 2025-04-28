from django.shortcuts import render
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    print("ok")
    if request.method=='POST':
        data = request.POST
        username = data.get("uname")
        email = data.get("email")
        phone = data.get("phone")
        age = data.get("age")

        st = student.objects.create(username=username,email=email,phone=phone,age=age)

        if(st):
            return render(request,'index.html',{'msg':"Registration successful"})

    return render(request,"index.html")