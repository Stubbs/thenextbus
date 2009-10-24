from django.http import HttpResponse
from google.appengine.api import urlfetch

def default(request, coords):
	"""Proxies the request through to the CloudMade API"""
	
	json = urlfetch.fetch("http://geocoding.cloudmade.com/b700b521f78b53b1b0e84cfabe192e6f/geocoding/geoobject_around_point/" + coords + "/500.js?object_type=bus_stop&return_location=true&return_geometry=false")
	return HttpResponse(json.content)