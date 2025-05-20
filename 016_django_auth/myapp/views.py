from django.shortcuts import render,redirect


from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def reg(request):
    return render(request,'reg.html')

@login_required(login_url='index')
def home(request):
    return render(request, 'home.html')

def register(request):

    try:
        if request.method == 'POST':
            # Process form data and register user
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['uname']
            email = request.POST['email']
            password = request.POST['pass']

            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username already exists.')
                return render(request,'reg.html')
            elif User.objects.filter(email=email).exists():
                messages.add_message(request, messages.ERROR, 'Email already exists.')
                return render(request,'reg.html')
            
            # Save user to the database
            user = User(first_name=fname, last_name=lname, username=username, email=email)
            user.set_password(password)  # Hash the password before saving it to the database
            user.save()

            messages.add_message(request, messages.SUCCESS, 'User registered successfully! you can now log in.')

            return render(request, 'reg.html')
        
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'An error occurred: {str(e)}')
        return render(request,'reg.html')
    
def user_login(request):
    try:
        if request.method == 'POST':
            username = request.POST['uname']
            password = request.POST['pass']

            user = authenticate(username=username, password=password)

            if user is not None:
                (login(request, user))
                
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid username or password.')
                return render(request, 'index.html')
            
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'An error occurred: {str(e)}')
        return render(request, 'index.html')
    
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'index.html')