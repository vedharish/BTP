from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list

urlpatterns = patterns('',
    url(r'^$', 'rawReq.manage.index'),
)
