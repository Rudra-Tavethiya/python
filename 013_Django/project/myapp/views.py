from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html", {'title':"Rudra | Index"})

def about(request):
    return render(request, "about.html", {'title':"Rudra | About"})

def contect(request):
    return render(request, "contect.html", {'title':"Rudra | Contect"})
