# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.


def index(request):
    return render(request, 'login/index.html')


def register(request):
    print request.POST
    User.objects.registerVal(request.POST)
    return HttpResponse()
