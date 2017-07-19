# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Error(object):
    def __init__(self, field, msg):
        self.field = field
        self.message = msg


class CourseManager(models.Manager):
    def add(self, data):
        errors = []
        if not data['name']:
            errors.append(Error('name', 'A course name is required'))
        if errors:
            return (False, errors)
        else:
            course = self.create(name=data['name'])
            Description.objects.create(course=course,
                                       description=data['description'])
            return (True, course)


class Course(models.Model):
    objects = CourseManager()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {} {} {}'.format(self.id, self.name, self.created_at, self.updated_at)

    def __unicode__(self):
        return '{}: {} {} {}'.format(self.id, self.name, self.created_at, self.updated_at)


class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def __unicode__(self):
        return self.description


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def __unicode__(self):
        return self.comment
