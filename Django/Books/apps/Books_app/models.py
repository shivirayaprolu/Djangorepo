# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
EMAILREG = re.compile(r'^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9.-_]+\.[a-zA-Z]*$')

class DBManager(models.Manager):
    def check_createauthor(self, data):
        errors = []
        if len(data['first_name']) < 2:
            errors.append(['first_name', "First Name must be at least two characters in length"])
        if len(data['last_name']) < 2:
            errors.append(['last_name', "Last Name must be at least two characters in length"])
        if not re.match(EMAILREG, data['email']):
            errors.append(['email', "Email must be a valid email address"])
        if errors:
            return [False, errors]
        else:
            current_author = AuthorDB.objects.filter(email=data['email'])
            if current_author:
                errors.append(['current_author', "Author is already exisiting in the database"])
                return [False, errors]
            newAuthor = AuthorDB(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])
            newAuthor.save()
            print("New Author is :")
            #print newAuthor
            return [True, newAuthor]

    def check_createbook(self, data):
        errors = []
        if len(data['title']) < 2:
            errors.append(['title', "Book Title must be at least two characters in length"])
        if len(data['category']) < 2:
            errors.append(['category', "Book Category must be at least two characters in length"])
        if errors:
            return [False, errors]
        else:
            current_book = BookDB.objects.filter(title=data['title'])
            if current_book:
                errors.append(['current_book', "Book with this title is already existing Please give a different name to the Book"])
                return [False, errors]
            newBook = BookDB(title=data['title'], category=data['category'], author=data['author'])
            newBook.save()
            #print newBook
            return [True, newBook]


class AuthorDB(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = DBManager()

class BookDB(models.Model):
    #book_author=models.ForeignKey(AuthorDB, related_name="book_author")
    title = models.CharField(max_length=50, blank=False)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = DBManager()

    def __str__(self):
        return 'ID: %s | Title of the Book: %s | Author: %s |Published date: %s' % (self.id, self.title, self.author, self.created_at)
