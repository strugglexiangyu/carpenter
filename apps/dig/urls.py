from coffin.conf.urls.defaults import *

urlpatterns = patterns('apps.dig.views',
    url(r'^save/$', 'save', name='dig_save'),
    url(r'^get/$', 'get', name='dig_get'),

)