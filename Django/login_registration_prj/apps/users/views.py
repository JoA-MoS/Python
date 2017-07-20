# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import User


# Create your views here.


def index(request):
    context = {'users': User.objects.all()}

    return render(request, 'users/list.html', context)


def registration(request):
    return render(request, 'users/registration.html')


@require_http_methods(['POST'])
def register(request):
    valid, data = User.objects.add(request.POST)
    if valid:
        print '---------------VALID-------------'
        print data
        return HttpResponse('User Created')
    else:
        print '============INVALID==========='
        print data
        for i in data:
            print i
            messages.add_message(request, messages.ERROR, i.message)
    # can we do this better
    return redirect('/users/registration')
