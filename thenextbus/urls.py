from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'thenextbus.stop.views.index'),
	(r'^redirect/$', 'thenextbus.stop.views.redirect'),
	(r'^help_nearby/$', 'thenextbus.stop.views.help_nearby'),
	(r'^stop/$', 'thenextbus.stop.views.redirect'),
	(r'^stop/add/$', 'thenextbus.stop.views.add_stop'),
	(r'^stop/edit/(?P<stop_number>\d+)$', 'thenextbus.stop.views.edit_stop'),
	(r'^stop/(?P<stop_number>\d+)/$', 'thenextbus.stop.views.stop'),
	(r'^proxy/(?P<coords>.*)/$', 'thenextbus.proxy.views.default'),
	(r'.*', 'thenextbus.stop.views.redirect'),
)
