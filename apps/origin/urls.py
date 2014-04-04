# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.origin.views',
    url(r'^index$', 'index', name='chart_index'),
    
)