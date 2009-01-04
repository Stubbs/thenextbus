from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'thenextbus.stop.views.index'),
	(r'^redirect/$', 'thenextbus.stop.views.redirect'),
	(r'^stop/$', 'thenextbus.stop.views.redirect'),
	(r'^stop/(?P<stop_number>\d+)/$', 'thenextbus.stop.views.stop'),
)
