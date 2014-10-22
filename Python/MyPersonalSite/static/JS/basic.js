/**
 * @author Sravan K Ghantasala
 */

window.onload = function(){
	// alert('Hi I am loaded');
}

function tab_click(topic) {
		$.post( '/home/', { 'transaction': 'topic','topic': topic } ).done ( function (data) {
			alert(JSON.stringify(data));
		} );
 };

function check_webPage(URL){
	if( ! _.isEmpty(URL)) return true;
	else return false;
}
function check_page(path){
	if( ! _.isEmpty(path)) return true;
	else return false;
}

function validate(data){
	// author, topic, tags and desc doesnt need any validation
	var error = ""
	// validating git link
	if(!check_webPage(data.gitlink)){
		document.getElementById("gitlinklabel").style.color = "red";
		error += "\nPlease enter a valid gitlink\n";
	}
	
	// Validating pagepath
	if(!check_page(data.pagepath)){
		document.getElementById("pagePathLabel").style.color = "red";
		error += "\nPlease enter a valid pagepath";
	}
	
	if (! _.isEmpty(error)) {
		alert("Error: " + error + "\n\nPlease enter all the highlighted fields...");
		return false;
	}
	else return true;
}

function submit_post(){
	form = document.getElementById("submitPostForm");
	d = {
		'transaction': 'submitpost', 
		'author' : form.elements.authorSelection.value,
		'topic' : form.elements.authorSelection.value,
		'tags' : $("#tags").tags().tagsArray,
		'gitlink' : form.elements.gitlink.value,
		'pagepath' : form.elements.pagePath.value,
		'desc' : form.elements.desc.value,					
	 };
	if(validate(d)){
		alert(JSON.stringify(d));
		// TODO: validate this form before submitting.
		// $.ajax({
			// url : "/home/", // Url from which we are requesting.
			// type : 'POST', // Type of the request
			// data : d, // Data to server
			// dataType : 'json', // Datatype expecting.
			// // Adding csrf token to the request header with out with django server
			// // fails to recognize the page and throws 403 forbidden error.
			// // beforeSend : function(xhr) {
				// // xhr.setRequestHeader("X-CSRFToken", $('#csrftoken').val());
			// // },
			// // Upon successfully retrieving data form the server
			// success : function(data, textStatus, jqXHR) {
				// alert(JSON.stringify(data));
			// },
			// error : function(jqXHR, status, error){
				// alert(status);
				// alert(error);
			// },
			// // This catches and alerts user based on the status code recieved form
			// // Django server. If the request was successful, Django returns code 200
			// // which needs no catching as it will directly go to success function.
			// statusCode : {
				// // This is the status code returned by Django server if it is
				// // not able to find the data requested information.
				// // might be data bot available or database not available
				// 500 : function() {
					// alert("Data requested is not available!");
				// },
				// // This is the satus code returned by Django server if it cannot
				// // process ajax request. Mainly caused with the csrf token mismatch
				// 403 : function() {
					// alert("Response error from Server...\n" + 
						// "CSRF mismatch error may be!");
				// }
			// }
		// })
		// .done(function() {alert("done")})
		// .fail(function(xhr,status, error)
		// {
			// alert(error);
			// alert(status);
		// })
		// ;
// 	
	
		$.post('/home/', d )
			.done( function(data){ alert(JSON.stringify(data)); })
			.fail(function(xhr,status, error) { alert(status);
												alert(error); })
		;
		
	}
	else{
		alert("Please fill all the mandatory fields!");
		return false;
	}
}

