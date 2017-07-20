# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import valid

# Create your models here.


class Error(object):
    def __init__(self, field, msg):
        self.field = field
        self.message = msg
        self.created_at = timezone.now()


class UserManager(models.Manager):
    def validate(self, data):
        errors = []
        if not valid.first_name(data['first_name']):
            errors.append(Error('first_name'))
        if errors:
            return (False, errors)
        else:
            return (True, data)

    def add(self, data):
        valid, errors = self.validate(data)
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
