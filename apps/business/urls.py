from coffin.conf.urls.defaults import *


urlpatterns = patterns('apps.business.views.business',
    url(r'^index/$', 'index', name='business_index'),
    url(r'^create/$', 'create', name='business_create'),
    url(r'^delete/$', 'delete', name='business_delete'),


)


