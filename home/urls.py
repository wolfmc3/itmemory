from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from home import views

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
]