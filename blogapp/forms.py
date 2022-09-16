from dataclasses import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CommentModel, Post


# forms classes

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label= 'confirm password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', "last_name", 'username', 'email']
        labels= {'email':'Email' }
    
            
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password =forms.CharField(label= 'password', widget=forms.PasswordInput)


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = CommentModel
        fields= ['comment',]
        
        def __str__(self):
            return self.comment

