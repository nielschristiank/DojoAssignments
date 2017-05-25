# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
    User.userManager.login("speros@codingdojo.com", "Speros")
    # return render(request, 'login/index.html')
    return HttpResponse (User.userManager.login("speros@codingdojo.com", "Speros"))
