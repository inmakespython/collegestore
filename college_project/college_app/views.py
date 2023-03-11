import email

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request,"home.html")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def fillform(request):
    return render(request,"fillform.html")

def form(request):
    return render(request,"form.html")

def msg(request):
    return render(request,"msg.html")

def logout(request):
    return redirect('/')

