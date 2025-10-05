from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from app import models
from app.models import TODO
from django.contrib.auth import login as lg,authenticate,logout


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
        name=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=name,password=password)
        if user is not None:
            lg(request,user)
            return redirect('/todo')
        else:
            return redirect('/login')
    return render(request,"login.html")

def todo(request):
    if request.method=='POST':
        title=request.POST.get("title")
        desc=request.POST.get("description")
        object=models.TODO(title=title,desc=desc,user=request.user)
        object.save()
        user=request.user
        res=models.TODO.objects.filter(user=request.user).order_by('date')
        return redirect("/todo",{'res':res})
    res=models.TODO.objects.filter(user=request.user).order_by('date')
    return render(request,"todo.html",{'res':res})

def edit(request,sno):
    if request.method=='POST':
        title=request.POST.get("title")
        desc=request.POST.get("description")
        object=models.TODO.objects.get(sno=sno)
        object.title=title
        object.desc=desc
        object.save()
        user=request.user
        res=models.TODO.objects.filter(user=request.user).order_by('date')
        return redirect("/todo",{'object':object})
    object=models.TODO.objects.get(sno=sno)
    res=models.TODO.objects.filter(user=request.user).order_by('date')
    return render(request,"edit_todo.html",{'object':object})

def delete(request,sno):
    object=models.TODO.objects.get(sno=sno)
    object.delete()
    return redirect("/todo")

def signout(request):
    logout(request)
    return redirect('/login')
# Create your views here.
