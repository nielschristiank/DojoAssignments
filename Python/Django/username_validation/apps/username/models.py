# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re

USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9.-_]{8,16}$')


# Create your models here.
class UserManager(models.Manager):
    def validate(self, request, username):
        validated = True
        # print username
        # usernames = User.objects.filter(username=username)
        # print usernames
        # print usernames['User']['username']
        # for name in usernames:
        #     if name['username'] == username:
        #         messages.add_message(request, messages.ERROR, 'username already taken')
        #         validated = False
        if not USERNAME_REGEX.match(username):
            messages.add_message(request, messages.ERROR, 'username must be between 8-16 characters, and contain only(a-z,A-Z,0-9, - , _ )')
            validated = False

        if validated == True:
            messages.add_message(request, messages.SUCCESS, 'The username: '+username+' is valid!')
        return validated

class User(models.Model):
    username = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
