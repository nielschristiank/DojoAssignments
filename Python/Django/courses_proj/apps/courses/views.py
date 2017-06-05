# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Course, Comment

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    Course.objects.create(name=request.POST['name'], description = request.POST['description'])
    print Course.objects.all()
    return redirect ('/')

def delete(request, id):
    # print id
    course = Course.objects.get(id=id)
    # print course.name
    context = {
        'course': course
    }
    return render(request, 'courses/delete.html', context)

def delete_course(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')

def view_course(request, id):
    print Comment.objects.all()
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/course.html', context)

def post_comment(request, id):
    course = Course.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], course_id=course)
    print Comment.objects.all()
    return redirect('view_course', id=course.id)
    # return redirect('/')
