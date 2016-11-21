$( "#steam" ).click(function() {
  var success = function( data ) {
    $( ".result" ).html( data );
    alert( "Load was performed." );
  };
  var error = function(error) {
	alert("An error happened");
  };
  $.get( "http://127.0.0.1:5000/dashboard/switch/steam", success, error);
});


