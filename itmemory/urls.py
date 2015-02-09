from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^objects/', include('objects.urls', namespace="objects")),
    url(r'^ittasks/', include('ittasks.urls', namespace="ittasks")),
    url(r'^customers/', include('customers.urls', namespace="customers")),
    url(r'^hwlogs/', include('hwlogs.urls', namespace="hwlogs")),
    url(r'^hpilo/', include('hpilo.urls', namespace="hpilo")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin_tools/', include('admin_tools.urls')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'}, name='mysite_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='mysite_logout'),
)
