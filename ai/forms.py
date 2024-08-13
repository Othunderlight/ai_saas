from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.forms import ModelForm
from django import forms
from .models import *




class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder':'Send or hold to talk...', 'id': 'messageInput'})
        } 
        labels = {
            'body': '',  # Set the label to an empty string
        }



        