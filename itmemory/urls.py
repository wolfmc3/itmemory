from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^$', include('home.urls', namespace="home")),
                       url(r'^objects/', include('objects.urls', namespace="objects")),
                       url(r'^ittasks/', include('ittasks.urls', namespace="ittasks")),
                       url(r'^customers/', include('customers.urls', namespace="customers")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                       url(r'^admin_tools/', include('admin_tools.urls')),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'}, name='mysite_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='mysite_logout'),
)
