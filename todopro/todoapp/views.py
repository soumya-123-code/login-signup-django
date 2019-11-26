from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        #check if a user exists
        #with the username and password
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'about.html')
        else:
            return render(request,'home.html',{'error':"Invalid Login Credentials"})
    else:
        return render(request,'home.html')

@login_required(login_url='/login')
def contact(request):
    return render(request,'contact.html')

@login_required(login_url='/login')
def blog(request):
    return render(request,'blog.html')


@csrf_exempt
def signup(request):
    if request.method == "POST":
        #create a user

        if request.POST['password'] == request.POST['passwordagain']:
            #both the password match
            # now the check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username']) 
                return render(request,'register.html',{'error': "Username has already been taken"})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                auth.login(request,user)  #registraion with direct login
                return redirect(home)
        

        else:
            return render(request,'register.html',{'error': "Password doesnot match"})
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect(home)