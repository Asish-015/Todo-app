from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from app.models import signup


def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create_user(name,email,password)
        user.save()
        # user=signup(username=name,email=email,password=password)
        # user.save()
        return redirect('/login')

    return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        user=User.objects.filter(username=name,password=password).first()
        if user is not None:
            return redirect('/todo')
        else:
            return redirect('/login')
    return render(request,"login.html")

def todo(request):
    return render(request,"todo.html")
# Create your views here.
