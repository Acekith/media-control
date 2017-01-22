var success = function( data ) {
	console.log('hiiii', data);
	$( ".result" ).html( data );
};
var error = function(error) {
	alert("An error happened");
};

$( "#steam" ).click(function() {
  $.get( "http://localhost:5000/dashboard/switch/Steam").done(success).fail(error);
});

$( "#kodi" ).click(function() {
  $.get( "http://localhost:5000/dashboard/switch/Kodi").done(success).fail(error);
});

$( "#netflix" ).click(function() {
  $.get( "http://localhost:5000/dashboard/switch/google-chrome").done(success).fail(error);
});
