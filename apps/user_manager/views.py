# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
import bcrypt
from .forms import *
from .models import *
# Create your views here.


#function for setting user session information
def set_session(request, status, user):
    request.session['user_id'] = user.id
    request.session['first_name'] = user.first_name
    request.session['name'] = user.first_name + " " + user.last_name
    
    request.session['status'] = status

#function for iterating through errors
def set_errors(request, errors):
    for tag, error in errors.iteritems():
        messages.error(request, error)

#renders login/reg page with respective forms
def log_reg(request):
    context = {
        'regForm': RegisterForm,
        'loginForm': LoginForm,
        'pWordForm': PasswordForm,
    }
    return render(request, 'user_manager/loginreg.html', context)

#processes login request, checks for errors in validator, if none logs in user and sets session
def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if errors:
            print errors
            set_errors(request, errors)
            return redirect(reverse('entry'))
        else:
            user = User.objects.get(username=request.POST['username'])
            set_session(request, "active", user)
            return redirect(reverse('home'))

#processes registration request, checks for errors in validator, if none adds user to database and logs in user, sets session
def reg(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if errors:
            set_errors(request, errors)
            return redirect(reverse('entry'))
        else:
            password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'], password=password,)
            user = User.objects.last()
            set_session(request, "new", user)
            return redirect('home')

#renders index page of all users, saved for reference but unlinked from application
def index(request):
    #test if visitor has logged in
    try:
        request.session['status']
    except KeyError:
        errors = {u'unregistered': u'You must log in before access!'}
        set_errors(request, errors)
        return redirect(reverse('entry'))
    #test if visitor is new
    if request.session['status'] == "active":
            text = "Welcome back"
    else:
            text = "Thanks for signing up"
    context = {
        "message" : text,
        "all_users" : User.objects.all(),
    }
    return render(request, 'user_manager/index.html', context)

#deletes user and refreshes index, saved for reference but not available in application
def delete(request, number):
    user = User.objects.get(id=number)
    user.delete()
    return redirect(reverse('index'))

#clears session, and logs user out bringing them to the login registration
def logout(request):
    request.session.clear()
    return redirect(reverse('entry'))
