# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=63, unique=True)
    description = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255)
    weight = models.FloatField()
    price = models.FloatField()
    cost = models.FloatField()
    category = models.ForeignKey(Category)
