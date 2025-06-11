from django.shortcuts import render
from myapp.models import *

# Create your views here.
def index(request):
    alldoctor = doctor.objects.all()
    return render(request,"index.html",{"alldoctors":alldoctor})

def contect(request):
    return render(request,"contect.html")