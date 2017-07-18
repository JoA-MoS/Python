# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, Http404

# Create your views here.


def index(request):
    # display instructions template
    return render(request, 'landscape/index.html')


def displayImage(request, imgNum):
    imgNum = int(imgNum)
    img = ''
    if isPrime(imgNum):
        img = 'randomImg'
    else:
        if 1 <= imgNum <= 10:
            img = 'snow'
        elif 11 <= imgNum <= 20:
            img = 'desert'
        elif 21 <= imgNum <= 30:
            img = 'forest'
        elif 31 <= imgNum <= 40:
            img = 'vineyard'
        elif 41 <= imgNum <= 50:
            img = 'tropical landscape'
        else:
            raise Http404
    context = {'image': img}
    return render(request, 'landscape/displayimage.html', context)


def isPrime(val):
    divisor = 2
    while divisor < val:
        print val % divisor
        if not (val % divisor):
            return False
        divisor += 1
    return True
