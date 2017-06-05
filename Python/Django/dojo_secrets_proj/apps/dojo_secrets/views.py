# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Secret, Like
from django.core.urlresolvers import reverse
import bcrypt, datetime
from django.db.models import Count

# Create your views here.
def index(request):
    print User.objects.all()
    return render(request, 'dojo_secrets/index.html')

def login(request):
    if request.method == "POST":
        login_valid = User.objects.login(request.POST)
        if 'errors' in login_valid:
            for error in login_valid['errors']:
                messages.error(request, error)
                return redirect('/')
        else:
            messages.success(request, 'Successfully Logged in')
            user = User.objects.get(id = login_valid['users'].id)
            request.session['logged_user'] = user.id
            return redirect(reverse('secrets'))
    return redirect('/')

def register(request):
    if request.method == "POST":
        errors = User.objects.register(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)

        else:
            messages.success(request, 'Successfully Registered. Please Login')
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(
                username=request.POST['username'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=hashed_pw
            )
    return redirect('/')

def secrets(request):
    if not 'logged_user' in request.session:
        return redirect('/')

    user_id = request.session.get('logged_user')
    context = {
        'user': User.objects.get(pk=user_id),
        'secrets': Secret.objects.all()
    }
    return render(request, 'dojo_secrets/secrets.html', context)

def popular_secrets(request):
    context = {
        'user': User.objects.get(pk=request.session.get('logged_user')),
        'secrets': Secret.objects.annotate(total_likes=Count('post_likes')).order_by('-total_likes')
    }
    return render(request, 'dojo_secrets/popular_secrets.html', context)

def post_secret(request):
    if not 'logged_user' in request.session:
        return redirect('index')
    if request.method == 'POST':
        user_id = request.session.get('logged_user')
        user = User.objects.get(pk=user_id)
        Secret.objects.create(user=user, post=request.POST['secret'])
    return redirect('secrets')

def like(request, secret_id):
    secret = Secret.objects.get(pk=secret_id)
    user = User.objects.get(pk=request.session.get('logged_user'))
    likes = Like.objects.filter(post=secret.id, user=user.id)
    print likes
    if not likes:
        Like.objects.create(post=secret, user=user)
    return redirect('secrets')

def delete_secret(request, id):
    Secret.objects.get(pk=id).delete()
    return redirect("secrets")

def logout(request):
    request.session.clear()
    return redirect("index")
