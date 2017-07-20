# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserManager(models.Manager):
    def registerVal(self, data):
        if 'f_name' not in data:
            if len(data['f_name'] < 3):
                print '***************not valid*****************'
        print type(data)
        print data


class User(models.Model):
    objects = UserManager()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return

    def __unicode__(self):
        return
