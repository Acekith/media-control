$( "#steam" ).click(function() {
  var success = function( data ) {
    $( ".result" ).html( data );
    alert( "Load was performed." );
  };
  var error = function(error) {
	alert("An error happened");
  };
  $.get( "/dashboard/switch/Steam", success, error);
});

$( "#kodi" ).click(function() {
  var success = function( data ) {
    $( ".result" ).html( data );
    alert( "Load was performed." );
  };
  var error = function(error) {
	alert("An error happened");
  };
  $.get( "/dashboard/switch/Kodi", success, error);
});

$( "#netflix" ).click(function() {
  var success = function( data ) {
    $( ".result" ).html( data );
    alert( "Load was performed." );
  };
  var error = function(error) {
	alert("An error happened");
  };
  $.get( "/dashboard/switch/google-chrome", success, error);
});
