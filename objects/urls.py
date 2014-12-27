from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from objects import views

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),
]