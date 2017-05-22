# -*- coding: utf-8 -*-
#CONTROLLER

from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

def index(request):
    print("*" * 100)
    return render(request, "first_app/index.html")

    # response = "Hello, I am your first request!"
    # return HttipResponse(response)



# Create your views here.
