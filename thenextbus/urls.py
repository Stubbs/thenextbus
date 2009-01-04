from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'thenextbus.stop.views.index'),
	(r'^stop/(?P<stop_number>\d+)/$', 'thenextbus.stop.views.stop'),
)
