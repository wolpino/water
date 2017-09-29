from django import forms
from django.forms import extras
import re, bcrypt
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=45, min_length=3)
    pword = forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45, min_length=3)
    last_name = forms.CharField(max_length=45, min_length=3)
    username = forms.CharField(max_length=45, min_length=3)
     
class PasswordForm(forms.Form):
    password = forms.CharField(max_length=100, min_length=8, widget=forms.PasswordInput)
    cpwd = forms.CharField(max_length=100, label="Confirm Password", widget=forms.PasswordInput)
