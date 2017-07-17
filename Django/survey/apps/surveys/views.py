# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def index(request):
    response = 'placeholder to display all the surveys created'
    return render(request,'surveys/index.html')


def new(request):
    response = 'placeholder for users to add a new survey'
    return HttpResponse(response)

def getSurvey(request, id):
    # do something with the ID to get a specific survery for now just ignoring
    return render(request, 'surveys/survey.html')

@require_http_methods(["POST"])
def processSurvey(request, id):
    print 'placeholder for processing a submitted survey with id {}'.format(id)
    
    print request.POST
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    
    

    # would get generated record ID for result

    return redirect('../results/{}'.format(1))

def getSurveyResults(request, id):
    response = 'placeholder for displaying Results to survey with id {}'.format(id)
    return HttpResponse(response)

def getSurveyResult(request, surveyId, resultId):
    print 'placeholder for displaying s specify result to a survey with id {} and a specific submission with id {}'.format(surveyId, resultId)
    return render(request, 'surveys/result.html')

