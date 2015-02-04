from django.conf.urls import url
from hpilo import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^upload/(?P<hwid>[0-9]+)/(?P<hwtoken>[\w]+)$', csrf_exempt(views.UploadView.as_view()), name='hpiloupload'),
]