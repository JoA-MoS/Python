# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Error(object):
    def __init__(self, field, msg):
        self.field = field
        self.message = msg


class BookManager(models.Manager):
    def add(self, data):
        errors = []
        if not data['title']:
            errors.append(Error('title', 'A title is required'))
        if not data['author']:
            errors.append(Error('author', 'An author is required'))
        if not data['category']:
            errors.append(Error('category', 'A category is required'))

        if errors:
            return (False, errors)
        else:
            book = self.create(title=data['title'],
                               author=data['author'],
                               category=data['category'],)
            return (True, book)


class Book(models.Model):
    objects = BookManager()
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {} {} {}'.format(self.id, self.title, self.author, self.category)

    def __unicode__(self):
        return '{}: {} {} {}'.format(self.id, self.title, self.author, self.category)
