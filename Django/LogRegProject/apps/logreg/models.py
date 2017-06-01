# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt, re
EMAILREG = re.compile(r'^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9.-_]+\.[a-zA-Z]*$')

class userDBManager(models.Manager):
    def hash_pass(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def check_create(self, data):
        errors = []
        if len(data['first_name']) < 2:
            errors.append(['first_name', "First Name must be at least two characters in length"])
        if len(data['last_name']) < 2:
            errors.append(['last_name', "Last Name must be at least two characters in length"])
        if not re.match(EMAILREG, data['email']):
            errors.append(['email', "Email must be a valid email address"])
        if len(data['password']) < 8:
            errors.append(['password', "Password must be at lease eight characters in length"])
        if not data['password'] == data['confirmpass']:
            errors.append(['confirmpass', "Passwords do not match"])
        if errors:
            return [False, errors]
        else:
            curent_user = UserDB.objects.filter(email=data['email'])
            if curent_user:
                errors.append(['curent_user', "Unable to register, please use alternate information"])
                return [False, errors]
            newUser = UserDB(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])
            # hashed_pass = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            # print hashed_pass, "hashed password"
            newUser.hashpw = self.hash_pass(data['password'].encode())
            print newUser.hashpw
            newUser.save()
            print newUser
            return [True, newUser]

    def check_log(self, data):
        errors = []
        curent_user = UserDB.objects.filter(email=data['email'])
        if not curent_user:
            errors.append(['account', "Email or password incorrect"])
        elif not bcrypt.checkpw(data['password'].encode(), curent_user[0].hashpw.encode()):
            errors.append(['account', "Email or password incorrect"])
        if errors:
            return [False, errors]
        else:
            return [True, curent_user[0]]

    def retrieveuser(self, data):
        errors = []
        curent_user = AuthorDB.objects.filter(id=data['id'])
        if errors:
            return [False, errors]
        else:
            return [True, curent_user[0]]

class UserDB(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    hashpw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = userDBManager()
    def __str__(self):
        return 'ID: %s | Name: %s %s | Email: %s' % (self.id, self.first_name, self.last_name, self.email)
