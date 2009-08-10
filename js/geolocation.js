function handler(location) {
	// Get the bus stops near here.
	var url = "http://geocoding.cloudmade.com/b700b521f78b53b1b0e84cfabe192e6f/geocoding/geoobject_around_point/" + location.coords.latitude + "," + location.coords.longitude + "/500.js?object_type=bus_stop";

	var x = new Ajax.Request(url, {
		method: 'get',
		onSuccess: function(transport) {
			alert(transport.status);
		},
		onFailure: function(transport) {
			alert("JHHJGJ");
		}});
}

function getLocation() {
	return navigator.geolocation.getCurrentPosition(handler)
}

// Add a listener to the "Near Me" button
Event.observe(window, 'load', function() {Event.observe('nearme_button', 'click', getLocation)});