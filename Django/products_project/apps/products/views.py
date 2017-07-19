# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Category, Product

# Create your views here.


def index(request):
    # use this method for inserting or getting the value with the matching unique name
    try:
        c = Category.objects.create(name='Tent',
                                    description='Tents')
    except:
        c = Category.objects.filter(name='Tent')[0]

    p = Product.objects.create(name='Kindom 4',
                               description='4 man tent',
                               weight=7.15,
                               price=400.25,
                               cost=200.25,
                               category=c)

    print p.category.name
    ps = Product.objects.all()
    for i in ps:
        print i.id, i.name

    return HttpResponse(c.id)
