from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>[0-9]+)/$', views.getSurvey),
    url(r'^(?P<id>[0-9]+)/process/$', views.processSurvey),
    url(r'^(?P<id>[0-9]+)/results/$', views.getSurveyResults),
    url(r'^(?P<surveyId>[0-9]+)/results/(?P<resultId>[0-9]+)/$', views.getSurveyResult),

]
