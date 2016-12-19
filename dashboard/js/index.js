$( "#steam" ).click(function() {
  var success = function( data ) {
    $( ".result" ).html( data );
    alert( "Load was performed." );
  };
  var error = function(error) {
	alert("An error happened");
  };
  $.get( "/dashboard/switch/steam", success, error);
});


