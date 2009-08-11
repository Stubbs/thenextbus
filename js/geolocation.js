function handler(location) {
	// Get the bus stops near here.
	var url = "/proxy/" + location.coords.latitude + "," + location.coords.longitude + "/";

	$.ajax({
		type: 'get',
		url: url,
		dataType: "json",
		success: function(data, text) { 
			$.each(data.features, function(i, item) {
				if(item.properties.ref) {
					$("#nearby_stops").append("<li><a href='/stop/" + item.properties.ref + "'>" + item.location.road + " (" + item.properties.ref + ")" + "</a></li>");
				} else {
					$("#nearby_stops").append("<li>" + item.location.road + "</li>");
				}
			})
		},
		error: function (XMLHttpRequest, textStatus, errorThrown) {
			alert(textStatus);
		}
		});
}

function getLocation() {
	$("#nearby_stops").text("");
	navigator.geolocation.getCurrentPosition(handler)
}

// Add a listener to the "Near Me" button
$(document).ready(function() {$("#nearme_button").bind("click", getLocation)});
