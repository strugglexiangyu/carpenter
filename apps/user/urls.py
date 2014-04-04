from coffin.conf.urls.defaults import *


urlpatterns = patterns('apps.user.views.user',
    url(r'^index/$', 'index', name='user_index'),
)


