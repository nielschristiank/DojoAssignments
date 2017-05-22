# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0;
    return render(request, 'ninjaGold/index.html')

def process_money(request):
    if 'message' not in request.session:
        request.session['message'] = []

    if request.POST['building'] == 'farm':
        randGold = random.randrange(10,20)
        request.session['gold'] += randGold
    if request.POST['building'] == 'cave':
        randGold = random.randrange(5,10)
        request.session['gold'] += randGold
    if request.POST['building'] == 'house':
        randGold = random.randrange(2,5)
        request.session['gold'] += randGold
    if request.POST['building'] == 'casino':
        randGold = random.randrange(-50,50)
        request.session['gold'] += randGold

    if randGold < 0:
        msg = ("red", str("Entered a "+request.POST['building']+" and lost "+str(randGold)+" gold...Ouch... "+"("+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")")))
    else:
        msg = ("green", str("Earned "+str(randGold)+" gold from the "+request.POST['building']+"! "+"("+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")")))

    request.session['message'].insert(0, msg)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
