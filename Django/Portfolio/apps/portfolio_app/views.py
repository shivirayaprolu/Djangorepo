# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
#from .models import UserDB

def index(request):
    return render(request, 'portfolio_app/index.html')
