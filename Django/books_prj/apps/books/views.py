# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Book

# Create your views here.


def index(request):
    Book.objects.create(title='test',
                        author='John',
                        published_date='2017-01-01')
    books = Book.objects.all()
    for b in books:
        print b.id, b.title, b.author
    return HttpResponse('index')
