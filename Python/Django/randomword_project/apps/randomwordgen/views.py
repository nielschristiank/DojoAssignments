# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import urllib2, random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
WORDS = urllib2.urlopen(word_site).read().splitlines()

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'randomwordgen/index.html')

def genWord(request):
    request.session['counter'] += 1
    request.session['word'] = random.choice(WORDS)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
