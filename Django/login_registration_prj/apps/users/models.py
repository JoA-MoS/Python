# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import isvalid
from error import Error

# Create your models here.


class UserManager(models.Manager):
    def validate(self, data):
        errors = []
        if 'first_name' in data and 'last_name' in data and 'email' in data and 'password' in data and 'c_password' in data:
            valid, msg = isvalid.first_name(data['first_name'])
            if not valid:
                errors.append(Error('first_name', msg))
            valid, msg = isvalid.last_name(data['last_name'])
            if not valid:
                errors.append(Error('last_name', msg))
            valid, msg = isvalid.email(data['email'])
            if not valid:
                errors.append(Error('email', msg))
            valid, msg = isvalid.password(
                data['password'], data['c_password'])
            if not valid:
                errors.append(Error('password', msg))
            # if all the fields look good make sure the user doesnt already exist
            if not errors:
                existing_users = self.filter(email=data['email'])
                if existing_users:
                    errors.append(Error(
                        'email', 'email already registered if you have forgoten your password please use the password reset link'))

        else:
            errors.append(
                Error('form', 'Something went wrong please try to submit the form again'))
        if errors:
            return (False, errors)
        else:

            return (True, data)

    def add(self, data):
        print data
        print 'strting validation'
        valid, errors = self.validate(data)
        print 'finished validation'
        if valid:
            return (valid, self.create(first_name=data['first_name'],
                                       last_name=data['last_name'],
                                       email=data['email'],
                                       password=data['password'],))
        else:
            return (valid, errors)


class User(models.Model):
    objects = UserManager()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {} {} {}'.format(self.id, self.first_name, self.last_name, self.email)

    def __unicode__(self):
        return '{}: {} {} {}'.format(self.id, self.first_name, self.last_name, self.email)
