# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import AuthorDB

def index(request, id):
    context = {
    "author": AuthorDB.objects.filter(id=id)
    }
    return render(request, 'portfolio_app/index.html',context)
