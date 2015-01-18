from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from hwlogs import views


urlpatterns = [
    url(r'^upload/$', views.UploadView.as_view(), name='upload'),
]