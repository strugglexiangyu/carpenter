from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

from settings import MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
 
    (r'^chart/', include('apps.chart.urls', namespace='chart', app_name='chart')),
    (r'^dig/', include('apps.dig.urls', namespace='dig', app_name='dig')),
    (r'^origin/', include('apps.origin.urls', namespace='origin', app_name='origin')),
	(r'^user/', include('apps.user.urls', namespace='user', app_name='user')),
	(r'^business/', include('apps.business.urls', namespace='business', app_name='business')),
    (r'^$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html'}),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
)

urlpatterns += staticfiles_urlpatterns()

