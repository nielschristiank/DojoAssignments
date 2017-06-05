# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import Count
import re, bcrypt
from django.utils import timezone

now = timezone.now()

#REGEX
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# any letter and -, min 2.
NAME_REGEX = re.compile(r'^^[a-zA-Z-]{2,}$')
# min 3, max 20 any letter, number or. -_
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9.\.-_]{3,20}$')
# 8-20 characters, 1 cap, 1 lower, 1 number, 1 symbol.
PW_REGEX = re.compile(r'^(?=.+?[A-Z])(?=.+?[a-z])(?=.+?[0-9])(?=.+?[!@#$%^&*()]).{8,20}$')

# MANAGERS
class UserManager(models.Manager):
    def login(self, postData):
        username = postData['username']
        password = postData['password']
        check_user = self.filter(username=username)
        login_valid = {}
        if check_user:
            print check_user
            user = check_user[0]
            print user.username
            hashed_pw = bcrypt.hashpw(password.encode(), user.password.encode())
            if user.password == hashed_pw:
                login_valid['users'] = user
                print user
                return login_valid
        login_valid['errors'] = ['Invalid username or password']
        return login_valid

    def register(self, postData):
        errors = [];
        check_user = self.filter(username=postData['username'])
        check_email = self.filter(email=postData['email'])
        if check_user:
            errors.append('username already exists')
        if check_email:
            errors.append('email already registered')
        if not USERNAME_REGEX.match(postData['username']):
            errors.append('Not a valid username')
        if not NAME_REGEX.match(postData['first_name']):
            errors.append('First name must be minimum 2 characters and can only contain letters')
        if not NAME_REGEX.match(postData['last_name']):
            errors.append('Last name must be minimum 2 characters and can only contain letters')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Not a valid email')
        if not PW_REGEX.match(postData['password']):
            errors.append('password must be minimum 8 characters, maximum 20, contain 1 uppercase letter, 1 lowercase letter, 1 number, and1 symbol (!@#$%^&*())')
        if postData['password'] != postData['passconf']:
            errors.append('passwords must match')
        return errors

class BookManager(models.Manager):
    def validate(self, postData):
        newAuthor = postData['new_author']
        existingAuthor = postData['existing_author']
        isValid = {
            'errors': [],
            # 'author': [],
            'newAuthor': [],
            'existingAuthor': []
        }
        if newAuthor and existingAuthor:
            isValid['errors'].append('Use only one Author Field. ')
        if not newAuthor and not existingAuthor:
            isValid['errors'].append('Author cannot be empty')
        if not postData['review']:
            isValid['errors'].append('Review cannot be empty')
        if not postData['title']:
            isValid['errors'].append('Book Title cannot be empty')
        if not postData['rating']:
            isValid['errors'].append('Rating cannot be empty')
        if newAuthor:
            check_author = Author.objects.filter(name=newAuthor)
            if check_author:
                isValid['errors'].append('Author already added')
            else:
                # authorAdded = Author.objects.create(name=newAuthor)
                isValid['newAuthor'].append(newAuthor)
        elif existingAuthor:
            # authorAdded = Author.objects.get(name=existingAuthor)
            isValid['existingAuthor'].append(existingAuthor)

        return isValid

# TABLES
class User(models.Model):
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="book_review")
    user = models.ForeignKey(User, related_name="user_review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    def stars(self):
        stars = ""
        for i in range(1,6):
            if i <= self.rating:
                # stars += "★"
                stars += u"\u2605"
            else:
                stars += u"\u2606"
                # stars += "&#9734;"
        return stars
