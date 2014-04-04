# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.chart.views',
    url(r'^index$', 'index', name='chart_index'),
    url(r'^pubuliu$', 'pubuliu', name='chart_pubuliu'),
    #url(r'^(?P<user_id>\d+)/auth/create$', 'create', name='auth_create'),
    #url(r'^(?P<user_id>\d+)/auth/(?P<gid>\d+)/update$', 'update', name='auth_update'),
    #url(r'^(?P<user_id>\d+)/auth/(?P<gid>\d+)/delete$', 'delete', name='auth_delete'),
)
