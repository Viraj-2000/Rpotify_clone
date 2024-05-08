from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def fun1(request):
    return render(request,'home.html')

def Signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        phone=request.POST.get('number')
        password=request.POST.get('password')
        rePassword=request.POST.get('confirm_pass')
        if not password==rePassword:
            return render(request,'signUp.html',{'error':"(Wrong Password)"})
        user=User.objects.create_user(email,phone,password)
        user.save()
        print(email,phone,password,rePassword)
        return redirect('/')
    return render(request,'signUp.html')

def login(request):
    if request.method=='POST':
         email=request.POST.get('email')
         password1=request.POST.get('password')
         user=authenticate(request,username=email,password=password1)
         if user is not None:
             return redirect('/')
    
        
    return render(request,'login.html')