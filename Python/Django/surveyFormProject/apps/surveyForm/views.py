# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'surveyForm/index.html')

def result(request):
    return render(request, 'surveyForm/result.html')

def process(request):
    request.session['surveyInfo'] = {
        'name': request.POST['name'],
        'favDChero': request.POST['favDChero'],
        'favMarvelhero': request.POST['favMarvelhero'],
        'comment': request.POST['comment']
        }
    print request.session['surveyInfo']
    return redirect('/result')
