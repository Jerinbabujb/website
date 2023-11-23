from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from pyexpat.errors import messages


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"inavalid ")
            return redirect('login')


    return  render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
            user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname,
                                        email=email)
            user.save();
            print("user created")
        else:
            print("password not matching")

    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
