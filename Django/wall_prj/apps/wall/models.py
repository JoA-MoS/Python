# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel

# Create your models here.


# class UserManger(models.Manager):
#     pass


class User(TimeStampedModel):
    # objects = UserManager()

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Message(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()


class Comment(TimeStampedModel):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
