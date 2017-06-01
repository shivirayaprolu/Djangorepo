# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserDB

def index(request):
    return render(request, 'logreg/index.html')

def log_register(request):
    if request.method == "POST":
        print request.POST
        if request.POST["chocolate"] == "register":
            response = UserDB.objects.check_create(request.POST)
        elif request.POST["chocolate"] == "login":
            response = UserDB.objects.check_log(request.POST)
        if not response[0]:
            for message in response[1]:
                messages.error(request, message[1])
            return redirect('logreg:index')
        else:
            request.session['user'] = {
            "id": response[1].id,
            "first_name": response[1].first_name,
            "last_name": response[1].last_name,
            }
            return redirect('logreg:home')
    return redirect('logreg:index')

def home(request):
    context = {
    "users": UserDB.objects.all()
    }
    return render(request, 'logreg/home.html', context)

def logout(request):
    request.session.clear()
    return redirect('logreg:index')
