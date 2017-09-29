# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..user_manager.models import User
from datetime import datetime

# Create your models here.
class TripManager(models.Manager):
    #trip validations    
    def trip_validator(self, postData):
        errors = {}
        #check if start date is in the past
        start_date = postData['start_date_year'] + "-" + postData['start_date_month'] + "-" + postData['start_date_day']
        if start_date < datetime.now().strftime("%Y-%m-%d"):
            errors['past'] = "You can't leave in the past!"
        #check the end is before the beginning        
        if postData['end_date_year'] < postData['start_date_year']:
            errors['backtofuture'] = "You can't return before you leave!!"
        if postData['end_date_year'] == postData['start_date_year']:
            if postData['end_date_month'] < postData['start_date_month']:
                errors['backtofuture'] = "You can't return before you leave!!"
        if postData['end_date_year'] == postData['start_date_year']:
            if postData['end_date_month'] == postData['start_date_month']:
                if postData['end_date_day'] < postData['start_date_day']:
                    errors['backtofuture'] = "You can't return before you leave!!"

        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    trip_planner = models.ForeignKey(User, related_name="trip_added")
    participants = models.ManyToManyField(User, related_name="trip_attending")    
    objects = TripManager()


