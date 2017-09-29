# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
from .forms import *
from .models import *
from ..user_manager.views import set_errors

# Create your views here.

#renders user's travel dashboard
def home(request):
#checks if visitor is logged in
    try:
        request.session['status']
    except KeyError:
        errors = {u'unregistered': u'You must log in before access!'}
        set_errors(request, errors)
        return redirect(reverse('entry'))
    id=request.session['user_id']
    context = {
        "all_trips" : Trip.objects.exclude(participants=id).all(),
        "all_users" : User.objects.all(),
        "user" : User.objects.filter(id=id),
        "joined_trips" : User.objects.get(id=id).trip_attending.all(),    
        }
    return render(request, 'meat/home.html', context)

def addtrip(request):
#checks if visitor is logged in
    try:
        request.session['status']
    except KeyError:
        errors = {u'unregistered': u'You must log in before access!'}
        set_errors(request, errors)
        return redirect(reverse('entry'))
#if user is logged in, display add trip form
    context = {
        'tripForm': TripForm,
    }
    return render(request, 'meat/addtrip.html', context)

#if trip passes validations, gets added to database and user gets added as a participant
def trip(request):
    if request.method == "POST":
        errors = Trip.objects.trip_validator(request.POST)
        if errors:
            set_errors(request, errors)
            return redirect(reverse('addtrip'))
        else:
            start_date = request.POST['start_date_year'] + "-" +request.POST['start_date_month'] + "-" + request.POST['start_date_day']
            end_date = request.POST['end_date_year'] + "-" +request.POST['end_date_month'] + "-" + request.POST['end_date_day']            
            Trip.objects.create(destination=request.POST['destination'], desc=request.POST['desc'], start_date=start_date, end_date=end_date, trip_planner_id=request.session['user_id'],)
            addparticipant = Trip.objects.last()
            addparticipant.participants.add(request.session['user_id'])
            addparticipant.save()
        return redirect('home')    

#displays trip information as well as list of participants not including the trip planner
def trip_page(request, number):
    trip = Trip.objects.get(id=number)
    context = {
        "destination": trip.destination,
        "planned_by" : User.objects.get(id=trip.trip_planner_id).first_name + " " + User.objects.get(id=trip.trip_planner_id).last_name,
        "desc": trip.desc,
        "start" : trip.start_date.strftime("%b %-d %Y"),
        "end" : trip.end_date.strftime("%b %-d %Y"),
        "all_participants" : Trip.objects.get(id=number).participants.exclude(id=trip.trip_planner_id)
    }
    return render(request, 'meat/trip.html', context)

#adds user to trip and moves trip to their trip list
def join(request, number):
    trip_to_join = Trip.objects.get(id=number)
    trip_to_join.participants.add(request.session['user_id'])
    trip_to_join.save()
    return redirect('home')    
