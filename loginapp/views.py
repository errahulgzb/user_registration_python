from django.shortcuts import render
from .models import User
import mysql.connector
from operator import itemgetter
from django.contrib import messages

# Create your views here.

def welcome(req):
    return render(req,'welcome.html')
    
def login(req):
    return render(req,'login.html')
    
    
def register(req):
    if req.method=="POST":
        user = User()
        
        user.fname=req.POST['fname']
        user.lname=req.POST['lname']
        user.email=req.POST['email']
        user.password=req.POST['password']
        user.re_password=req.POST['re_password']
        if user.password != user.re_password:
            return redirect('register')
        elif user.fname =="" or user.password =="":
            messages.info(req,'some fields are empty.')
        else:
            user.save()
    return render(req,'register.html')