from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
#from .models import UserDB

def index(request):
    return render(request, 'LoginRegisteration_app/index.html')


# Create your views here.
