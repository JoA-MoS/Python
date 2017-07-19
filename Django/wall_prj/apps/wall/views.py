# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.


def index(request):
    u = User.objects.create(first_name='Justin',
                            last_name='Dietz',
                            email='justin.r.dietz@gmail.com')
    print u
    return HttpResponse('index')
