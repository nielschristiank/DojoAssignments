# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'username/index.html')

def userpage(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'username/user.html', context)

def add_user(request):
    validated = User.objects.validate(request, request.POST['username'])
    if validated == True:
        User.objects.create(username=request.POST['username'])
        # request.session['user'] =
        return redirect('/userpage')
    else:
        return redirect('/')
