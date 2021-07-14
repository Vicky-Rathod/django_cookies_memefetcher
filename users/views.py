from django import forms
from django.shortcuts import render, redirect
from .forms import UserSignUpForm 
from django.contrib import messages
from .models import User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import get_template
from django_email_verification import send_email

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.is_active = False # Example
            send_email(user)
            ##################################################################
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            return HttpResponse(form.errors)
    else:
        
        form = UserSignUpForm()
    return render(request, 'user/register.html', {'form': form, 'title':'reqister here'})


