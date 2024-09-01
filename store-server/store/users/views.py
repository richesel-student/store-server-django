from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from users.models import User
from users.forms import UserLoginForm
from django.urls import reverse
from users.forms import  UserLoginForm, UserRegistrationForm

def login(reqest):
    if reqest.method == 'POST':
        form = UserLoginForm(data=reqest.POST)
        if form.is_valid():
            username = reqest.POST['username']
            password = reqest.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(reqest, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(reqest, 'users/login.html', context)

def registration(reqest):
    form = UserRegistrationForm()
    context = {'form': form}
    return render(reqest, 'users/registration.html', context)

# Create your views here.
