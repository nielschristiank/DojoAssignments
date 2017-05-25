# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import books

# Create your views here.
def index(request):
    context = {
        'books': books.objects.all()
    }
    return render(request, 'books/index.html', context)

def submit_book(request):
    books.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')
