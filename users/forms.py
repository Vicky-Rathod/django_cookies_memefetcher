
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    
    class Meta:
        model = User
        fields = ('username','email','phone', 'first_name','last_name','address','password1','password2')
