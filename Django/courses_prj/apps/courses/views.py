# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Course, Description, Comment


# Create your views here.


def index(request):

    context = {'courses': Course.objects.all()}
    # descriptions = Description.objects.all()

    return render(request, 'courses/index.html', context)


@require_http_methods(['POST'])
def addCourse(request):
    valid, data = Course.objects.add(request.POST)
    if valid:
        print valid
        print data
    else:
        for i in data:
            messages.add_message(request, messages.ERROR, i.message)

    return redirect('/courses')


def confirmDelete(request, courseId):
    context = {'course': Course.objects.get(id=courseId)}
    return render(request, 'courses/confirm_course_delete.html', context)


@require_http_methods(['DELETE'])
def deleteCourse(request, courseId):
    Course.objects.get(id=courseId).delete()
    return JsonResponse(status=200)
