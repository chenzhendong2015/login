#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from login.models import Person
import time
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def check_name(request):
    userName = request.GET.get("userName",None)

    status = 1
    p = Person.objects
    post = p.all()

    for e in post:
        if (e.userName == userName):
            status = 2
            break
    return HttpResponse(status)

def check_email(request):
    email = request.GET.get("email", None)

    status = 1
    p = Person.objects
    post = p.all()

    for e in post:
        if (e.email == email):
            status = 2
            break

    return HttpResponse(status)



def regcheck(request):
    userName = request.GET.get("userName",None)
    email = request.GET.get("email",None)
    password = request.GET.get("password",None)

    status = 1
    p = Person.objects
    post = p.all()

    for e in post:
        if(e.userName==userName or e.email==email):
            status = 2
            break
    if(status==1):
        now = int(time.time())
        userId = ""+now.__str__()
        p.create(userName = userName, email = email, password = password, userId = userId)
        print("add successfully")
    return HttpResponse(status)

def logcheck(request):
    email = request.GET.get("email",None)
    password = request.GET.get("password",None)

    status = 1
    p = Person.objects
    post = p.all()

    for e in post:
        if(e.password==password and e.email==email):
            return HttpResponse(e.userId)
            break
    return HttpResponse(status)

def success(request):
    userId = request.GET.get("userId",None)

    p = Person.objects
    post = p.all()
    for e in post:
        print(e.userId + " == " + userId)
        if (e.userId == userId):
            print(e.userName + "登录")
            return render(request, "success.html", {'userName': e.userName, "email":e.email, "userId":userId})
            break