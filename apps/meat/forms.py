from django import forms
from django.forms import extras
import re, bcrypt
from .models import *
import datetime

years_to_display = range(datetime.datetime.now().year, datetime.datetime.now().year + 50)

class TripForm(forms.Form):
    destination = forms.CharField(max_length=45, min_length=3)
    desc = forms.CharField(max_length=45, min_length=3)
    start_date = forms.DateField(label=("Travel Date From:"), widget=extras.SelectDateWidget(years=years_to_display), required=True)
    end_date = forms.DateField(label=("Travel Date To:"), widget=extras.SelectDateWidget(years=years_to_display), required=True)
