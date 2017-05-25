# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt, datetime

# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def user(request):
    return render(request, 'login_registration/user.html')

def login(request):
    if request.method == "POST":
        login_valid = User.objects.login(request.POST)
        if 'errors' in login_valid:
            for error in login_valid['errors']:
                messages.error(request, error)
                return redirect('/')
        else:
            messages.success(request, 'Successfully Logged in')
            user = User.objects.get(id = login_valid['users'].id)
            # request.session['logged_user'] = user.id
            request.session['logged_user'] = {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'birthday': str(user.birthday),
            }
            print request.session['logged_user']['birthday']
            return redirect('/user')
    return redirect('/')

def register(request):
    if request.method == "POST":
        errors = User.objects.register(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)

        else:
            messages.success(request, 'Successfully Registered. Please Login')
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(
                username=request.POST['username'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                birthday=request.POST['birthday'],
                password=hashed_pw
            )
            # return redirect('/')
    return redirect('/')
