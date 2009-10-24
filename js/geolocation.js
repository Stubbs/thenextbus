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
					if(item.properties["naptan:AtcoCode"]) {
						// HACK: Remove the third character, Naptan codes have too many 0's in them.
						$("#nearby_stops").append("<li><a href='/stop/" + item.properties["naptan:AtcoCode"].replace('00', '0') + "'>" + item.properties["name"] + " (" + item.properties["naptan:AtcoCode"] + ")" + "</a></li>");
					}
					// If there's no Naptan data, maybe someone added the stop?
					else if(item.properties.ref) {
						$("#nearby_stops").append("<li><a href='/stop/" + item.properties.ref + "'>" + item.location.road + " (" + item.properties.ref + ")" + "</a></li>");
					// Failing that, just print the name of the stop.
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
