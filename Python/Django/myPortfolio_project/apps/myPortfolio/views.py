# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myPortfolio/index.html')

def projects(request):
    return render(request, 'myPortfolio/projects.html')

def aboutme(request):
    return render(request, 'myPortfolio/aboutme.html')

def testimonials(request):
    return render(request, 'myPortfolio/testimonials.html')
