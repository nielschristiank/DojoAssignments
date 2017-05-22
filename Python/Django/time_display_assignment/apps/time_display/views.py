# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
import datetime

# now = datetime.datetime.now()

# Create your views here.
def index(request):
    current_time = {'current_time': datetime.datetime.now().strftime('%c')}
    return render(request, 'time_display/index.html', current_time)
