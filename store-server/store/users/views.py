from django.shortcuts import render

def login(reqest):
    return render(reqest, 'users/login.html')

def registration(reqest):
    return render(reqest, 'users/registration.html')

# Create your views here.
