from django.shortcuts import render

from users.models import User
from users.forms import UserLoginForum

def login(reqest):
    context = {'form': UserLoginForum()}
    return render(reqest, 'users/login.html', context)

def registration(reqest):
    return render(reqest, 'users/registration.html')

# Create your views here.
