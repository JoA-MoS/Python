# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Book, Error

# Create your views here.


def index(request):

    context = {'books': Book.objects.all()}

    return render(request, 'books/index.html', context)


@require_http_methods(['POST'])
def addBook(request):

    valid, data = Book.objects.add(request.POST)
    if valid:
        print valid
        print data
    else:
        for i in data:
            messages.add_message(request, messages.ERROR, i.message)

    return redirect('/books')
