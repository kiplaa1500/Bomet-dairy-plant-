from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']
        
class notificationsForm(forms.ModelForm):
    class Meta:
        model=Notifications
        exclude=[]


class dailyrecordsForm(forms.ModelForm):
    class Meta:
        model=Dailyrecords
        exclude=[]
        

class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        exclude=['owner','neighbourhood']
