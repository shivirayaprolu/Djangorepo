# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import AuthorDB, BookDB

def index(request):
    alldata = {
    "books": BookDB.objects.all(),
    "all_authors": AuthorDB.objects.all()
    }
    #print alldata
    return render(request, 'Books_app/index.html', alldata)

def addauthor(request):
    if request.method == "POST":
        response = AuthorDB.objects.check_createauthor(request.POST)
        print request.POST
    if not response[0]:
        for message in response[1]:
            messages.error(request, message[1])
        #return redirect('Books:index')
    else:
        request.session['author'] = {
        "id": response[1].id,
        "first_name": response[1].first_name,
        "last_name": response[1].last_name,
        }
        #return redirect('Books:index')
    return redirect('Books:index')

def addbook(request):
    if request.method == "POST":
        response = BookDB.objects.check_createbook(request.POST)
        print request.POST
    if not response[0]:
        for message in response[1]:
            messages.error(request, message[1])
        #return redirect('Books:index')
    else:
        request.session['books'] = {
        "id": response[1].id,
        "title": response[1].title,
        "category": response[1].category,
        "author": response[1].author,
        }
        #return redirect('Books:index')
    return redirect('Books:index')
