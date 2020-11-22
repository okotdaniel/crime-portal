from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import *


class reportSuspectForm(ModelForm):
    class Meta:
        model = ReportSuspect
        fields = '__all__'

class reportCrimeForm(ModelForm):
    class Meta:
        model = ReportCrimeModel
        fields ='__all__'


class createUserForm(UserCreationForm): 
    class Meta:
        model = User 
        fields = ['username', 'email' , 'password1','password2']

