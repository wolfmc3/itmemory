from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from customers import views

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^import/$', login_required(views.ImportCustomer.as_view()), name='import'),
    url(r'^import/add/$', login_required(views.import_add), name='add'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),
]