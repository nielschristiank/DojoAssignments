# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Blogs, Comments

# Create your views here.
def index(request):
    context = {
        "blogs": Blogs.objects.all()
    }
    return render(request, 'test_app/index.html', context)

def blogs(request):
    # using ORM
    Blogs.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    return redirect('/')

def comments(request, id):
    blog = Blogs.objects.get(id=id)
    Comments.objects.create(comment=request.POST['comment'], blog_id=blog)
    return redirect('/')
