from django.shortcuts import render,redirect
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':

        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['pass']

        if User.objects.filter(username=uname).exists():
            return render(request, 'index.html', {'error': 'Username already exists'})
        
        elif User.objects.filter(email=email).exists():
            return render(request, 'index.html', {'error': 'Email already exists'})
        

        # Add user to database
        user = User(username=uname, email=email,first_name = fname, last_name = lname)
        user.set_password(password)
        user.save()

        return render(request, 'home.html')
    
    return render(request,'index.html')
    

    

def home(request):
    return render(request, 'home.html')
        
        

def signup(request):
    return render(request, 'index.html')

def login(request):

    if request.user.id is None:
        return render(request, 'login.html')
    else:
        return redirect('home')


def logout(request):
    return redirect('index')