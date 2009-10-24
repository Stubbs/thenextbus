function handler(location) {
	// Get the bus stops near here.
	var url = "/proxy/" + location.coords.latitude + "," + location.coords.longitude + "/";

	$.ajax({
		type: 'get',
		url: url,
		dataType: "json",
		success: function(data, text) { 
			if(data.found > 0) {
				$.each(data.features, function(i, item) {
					if(item.properties.ref) {
						$("#nearby_stops").append("<li><a href='/stop/" + item.properties.ref + "'>" + item.location.road + " (" + item.properties.ref + ")" + "</a></li>");
					} else {
						$("#nearby_stops").append("<li>" + item.location.road + "</li>");
					}
				})
			} else {
				$("#nearby_stops").append("Couldn't find any stops nearby.");
			}
		},
		error: function (XMLHttpRequest, textStatus, errorThrown) {
			alert(textStatus);
		}
		});
}

function noLocation() {
	$("#nearby_stops").html("Your device doesn't appear to support the location API.");
};

function getLocation() {
	$("#nearby_stops").text("");
	if(navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(handler, noLocation)
	} else {
		$("#nearby_stops").html("Your device doesn't appear to support the location API.");
	}
}

// Add a listener to the "Near Me" button
$(document).ready(function() {$("#nearme_button").bind("click", getLocation)});
