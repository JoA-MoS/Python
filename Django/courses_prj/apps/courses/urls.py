from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.addCourse),
    url(r'^(?P<courseId>\d+)/confirm-delete/', views.confirmDelete),
    url(r'^(?P<courseId>\d+)/delete/', views.deleteCourse),
]
