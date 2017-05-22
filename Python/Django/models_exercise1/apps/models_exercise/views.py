# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import People

# Create your views here.
def index(request):
    People.objects.create(first_name="Bruce", last_name="Wayne")
    people = People.objects.all()
    print people
    return render(request, 'models_exercise/index.html')
