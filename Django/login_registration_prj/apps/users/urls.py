from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/', views.registration),
    url(r'^register/', views.register),
    url(r'^login/$', views.showLogin),
    url(r'^login/process/$', views.login),
]
