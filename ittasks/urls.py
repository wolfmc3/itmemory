from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ittasks import views

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<pk>[0-9]+)/setenable$', views.setenabledtask, name='setenabledtask'),
    url(r'^(?P<pk>[0-9]+)/updatechecks$', views.updatechecks, name='updatechecks'),
    url(r'^(?P<pk>[0-9]+)/updateuser$', views.updateuser, name='updateuser'),
    url(r'^(?P<pk>[0-9]+)/close$', views.closetask, name='closetask'),
    url(r'^calendar/(?P<month>[0-9]+)/(?P<year>[0-9]+)$', views.calendar, name='calendar'),
]