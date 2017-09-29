# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    #registration validations    
    def reg_validator(self, postData):
        #check if username is already in the database, pass if not       
        errors = {}
        try:
            User.objects.get(username=postData['username'])
            errors["active"] = "You've already registered, please log in"
            return errors 
        except User.DoesNotExist:
            pass
        #check if there are any non letter character in the first and last names        
        if any(i.isalpha() is False for i in postData['first_name']):
            errors["digits"] = "Name can only contain letters " 
        #check password and password confirmation match                            
        if postData['password'] != postData['cpwd']:
            errors["cpwd_comf"] = "Passwords do not match"       
        return errors

    #login validations    
    def login_validator(self, postData):
        errors = {}
        username = postData['username']
        password = postData['pword'].encode()
        #check if user is in database    
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            errors["reg"] = "Please register first"
            return errors
        #check if password is correct    
        if bcrypt.checkpw(password.encode(), user.password.encode()) is False:
            errors["incorrect"] = "Incorrect password!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)   
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
   