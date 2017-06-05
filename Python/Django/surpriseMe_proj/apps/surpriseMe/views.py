# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import urllib2, random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
WORDS = urllib2.urlopen(word_site).read().splitlines()

# WORDS = ['banana', 'apple', 'butthole','star wars','batman', 'robin', 'poop']

# Create your views here.
def index(request):
    request.session.clear()
    return render(request, 'surpriseMe/index.html')

def results(request):
    return render(request, 'surpriseMe/results.html')

def randomWords(request):
    num = int(request.POST['num'])
    request.session['words'] = []
    while num > 0:
        # print "step 2"
        num -= 1;
        newWord = random.choice(WORDS)
        request.session['words'].append(newWord)
    return redirect('/results')
