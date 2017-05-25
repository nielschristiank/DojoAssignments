# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# our Manager
class UserManager(models.Manager):
  def login(self, email, password):
      print "login logic here!"
      print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
      print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"
      return ("I will be a futute login method")

  def register(self, **kwargs):
      print ("Register a user here")
      print ("If successful, maybe return {'theuser':user} where user is a user object?")
      print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")
# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  password = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  # *************************
  # Connect an instance of UserManager to our User model overwriting
  # the old hidden objects key with a new one with extra properties!!!
  userManager = UserManager()
  # *************************
