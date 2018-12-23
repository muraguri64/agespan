from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        #user has info and wants account now
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(email=request.POST['email'])
                return render(request,'accounts/signup.html',{'error':'Email has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(email=request.POST['email'],username=request.POST['email'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'Passwords must match!'})
    else:
        # user wats to enter info
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request,'accounts/signup.html')

        



def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'Email or Password is Incorrect!'})

    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request,'accounts/login.html')
        


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
