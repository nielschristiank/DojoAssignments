# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt, datetime


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^^[a-zA-Z-]{2,}$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9.-_]{3,}$')
PW_REGEX = re.compile(r'^(?=.+?[A-Z])(?=.+?[a-z])(?=.+?[0-9])(?=.+?[!@#$%^&*()]).{8,20}$')

class UserManager(models.Manager):
    def login(self, postData):
        username = postData['username']
        password = postData['password']
        check_user = self.filter(username=username)
        login_valid = {}
        # success = []
        if check_user:
            print check_user
            user = check_user[0]
            print user.username
            hashed_pw = bcrypt.hashpw(password.encode(), user.password.encode())
            if user.password == hashed_pw:
                # success.append('Successful Login')
                login_valid['users'] = user
                print user
                return login_valid
        login_valid['errors'] = ['Invalid username or password']
        return login_valid

    def register(self, postData):
        username = postData['username']
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        birthday = postData['birthday']
        password = postData['password']
        passconf = postData['passconf']

        errors = [];

        check_user = self.filter(username=username)
        check_email = self.filter(email=email)

        if check_user:
            errors.append('username already exists')
        if check_email:
            errors.append('email already registered')
        if not USERNAME_REGEX.match(username):
            errors.append('Not a valid username')
        if not NAME_REGEX.match(first_name):
            errors.append('First name must be minimum 2 characters and can only contain letters')
        if not NAME_REGEX.match(last_name):
            errors.append('Last name must be minimum 2 characters and can only contain letters')
        if not EMAIL_REGEX.match(email):
            errors.append('Not a valid email')
        if not birthday:
            errors.append('birthday cannot be blank')
        if not PW_REGEX.match(password):
            errors.append('password must be minimum 8 characters, maximum 20, contain 1 uppercase letter, 1 lowercase letter, 1 number, and1 symbol (!@#$%^&*())')
        if password != passconf:
            errors.append('passwords must match')

        return errors

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    birthday = models.DateField(null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
