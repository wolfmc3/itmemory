from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from hpilo import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^upload/(?P<hwid>[0-9]+)/(?P<hwtoken>[\w]+)$', csrf_exempt(views.UploadView.as_view()), name='hpiloupload'),
    url(r'^pack/(?P<hwid>[0-9]+)$', login_required(views.CreatePack.as_view()), name='createpack'),
]