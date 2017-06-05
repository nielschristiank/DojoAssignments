# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User, Book, Author, Review
from django.contrib import messages
from django.db.models import Count
import bcrypt

# Create your views here.
def index(request):
    if 'logged_user' in request.session:
        return redirect(reverse('home'))
    return render(request, 'beltreview/index.html')

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

def login(request):
    if request.method == "POST":
        login_valid = User.objects.login(request.POST)
        if 'errors' in login_valid:
            for error in login_valid['errors']:
                messages.error(request, error)
                return redirect('/')
        else:
            # messages.success(request, 'Successfully Logged in')
            user = User.objects.get(id = login_valid['users'].id)
            # request.session['logged_user'] = user.id
            request.session['logged_user'] = user.id
            # {
            #     'id': user.id,
            #     'username': user.username,
            #     'first_name': user.first_name,
            #     'last_name': user.last_name
            # }
            return redirect('home')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect(reverse('index'))

def home(request):
    user_id = request.session.get('logged_user')
    if not user_id:
        return redirect ('/')
    context = {
        'user': User.objects.get(pk=user_id),
        'books': Book.objects.all().order_by('title'),
        'reviews': Review.objects.all().order_by('-created_at')[:3]
    }
    return render(request, 'beltreview/home.html', context)

def show_add_book(request):
    user_id = request.session.get('logged_user')
    if not user_id:
        return redirect ('index')

    context = {
        "user": User.objects.get(pk=user_id),
        "authors": Author.objects.all()
    }

    return render(request, 'beltreview/addbook.html', context)


def add_book(request):
    isValid = Book.objects.validate(request.POST)
    if isValid['errors']:
        for error in isValid['errors']:
            messages.error(request, error)
        return redirect('show_add_book')

    if isValid['newAuthor']:
        newAuthor = isValid['newAuthor'][0]
        author = Author.objects.create(name=newAuthor)
    if isValid['existingAuthor']:
        existingAuthor = isValid['existingAuthor'][0]
        author = Author.objects.get(name=existingAuthor)

    user_id = request.session['logged_user']
    user = User.objects.get(id=user_id)
    # author = isValid['author'][0]
    newBook = Book.objects.create(title=request.POST['title'], author=author)
    newReview = Review.objects.create(content=request.POST['review'], rating=request.POST['rating'], book=newBook, user=user)
    return redirect(reverse('show_book', kwargs={'id': newBook.id}))

def show_book(request, id):
    user_id = request.session['logged_user']
    if not user_id:
        return redirect ('index')
    context = {
        'user': User.objects.get(id=user_id),
        'book': Book.objects.get(id=id),
        'reviews': Review.objects.filter(book=id)
    }
    return render(request, 'beltreview/book.html', context)

def add_review(request, id):
    if request.method == 'POST':
        user_id = request.session['logged_user']
        check_review = Review.objects.filter(book=id, user=user_id)
        if check_review:
            messages.error(request, 'You already reviewed this book!')
            return redirect(reverse('show_book', kwargs={'id':id}))
        if not request.POST['review']:
            messages.error(request, 'cannot be blank')
            return redirect(reverse('show_book', kwargs={'id':id}))
        if not request.POST['rating']:
            messages.error(request, 'must have rating')
            return redirect(reverse('show_book', kwargs={'id':id}))
        user = User.objects.get(pk=request.session['logged_user'])
        book = Book.objects.get(pk=id)
        newReview = Review.objects.create(content=request.POST['review'], rating=request.POST['rating'], book=book, user=user)
    return redirect(reverse('show_book', kwargs={'id':id}))

def delete_review(request, id):
    user_id = request.session.get('logged_user')
    if not user_id:
        return redirect ('index')
    print request.get_full_path
    url_redirect = request.META['HTTP_REFERER']
    print url_redirect

    Review.objects.get(pk=id).delete()
    return redirect(url_redirect)

def show_user(request, id):
    user_id = request.session.get('logged_user')
    if not user_id:
        return redirect ('index')
    found_user = User.objects.get(id=id)
    # print found_user
    context = {
        'user': found_user,
        'reviews': Review.objects.filter(user=found_user.id),
    }
    # print user
    # print user['id'], user['username']
    return render(request, 'beltreview/user.html', context)
