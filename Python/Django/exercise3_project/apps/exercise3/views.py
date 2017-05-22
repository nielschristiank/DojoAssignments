# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'email': 'blob@gmail.com',
        'name': 'mike'
    }
    return render(request, 'exercise3/index.html', context)

def show(request, id):
    context = {
        'id': id
    }
    return render(request, 'exercise3/show.html', context)
