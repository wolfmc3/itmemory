from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from objects import views

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<pk>[0-9]+)/pwd$', login_required(views.getpassword), name='getpassword'),
    url(r'^(?P<pk>[0-9]+)/act_task/(?P<task>[0-9]+)$', login_required(views.createtask), name='createtask'),
    url(r'^(?P<objid>[0-9]+)/addpassword$', login_required(views.PasswordCreate.as_view()), name='addpassword'),
    url(r'^(?P<objid>[0-9]+)/password/(?P<pk>[0-9]+)$', login_required(views.PasswordUpdate.as_view()),
        name='password'),
    url(r'^(?P<objid>[0-9]+)/addsetting$', login_required(views.SettingCreate.as_view()), name='addsetting'),
    url(r'^(?P<objid>[0-9]+)/setting/(?P<pk>[0-9]+)$', login_required(views.SettingUpdate.as_view()), name='setting'),
]