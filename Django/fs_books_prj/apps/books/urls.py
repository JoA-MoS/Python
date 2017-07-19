from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.addBook),
    # url(r'^admin/', admin.site.urls),
]
