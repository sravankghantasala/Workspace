/**
 * @author Sravan K Ghantasala
 */

window.onload = function(){
	// alert('Hi I am loaded');
}

function tab_click(topic) {
        // var target = getEventTarget(event);
        alert(topic);
        // $.ajax({
			// type: "POST",
			// url: /home/,
			// data: topic,
			// success: success,
			// dataType: d
		// });
		$.post( '/home/', { 'transaction': 'topic','topic': topic } ).done ( function (data) {
			alert(JSON.stringify(data));
		} );
 };
 
function submit_post(form){
	d = {
		'transaction': 'submitpost', 
		'author' : form.elements.authorSelection.value,
		'topic' : form.elements.authorSelection.value,
		'tags' : $("#tags").tags().tagsArray,
		'gitlink' : form.elements.gitlink.value,
		'pagepath' : form.elements.pagePath.value,
		'desc' : form.elements.desc.value,					
	 };
	alert(JSON.stringify(d))
	// $.ajax({
		// url : '/dcm/', // Url from which we are requesting.
		// type : 'POST', // Type of the request
		// data : {
			// 'transaction' : 'submit post',
			// 'data' : postdata
		// }, // Data to server
		// dataType : 'json', // Datatype expecting.
		// // Adding csrf token to the request header with out with django server
		// // fails to recognize the page and throws 403 forbidden error.
		// // beforeSend : function(xhr) {
			// // xhr.setRequestHeader("X-CSRFToken", $('#csrftoken').val());
		// // },
		// // Upon successfully retrieving data form the server
		// success : function(data, textStatus, jqXHR) {
			// alert(data);
		// },
		// error : function(jqXHR, status, error){
			// alert(status);
			// alert(error);
		// },
		// // This catches and alerts user based on the status code recieved form
		// // Django server. If the request was successful, Django returns code 200
		// // which needs no catching as it will directly go to success function.
		// complete : function(jqXHR, status){
			// alert(status);
			// alert(jqXHR.status);
		// },
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
	// }).done(function);


	$.post('/home/', d )
		.done( function(data){ alert(JSON.stringify(data)); })
		.fail(function(xhr,status, error) { alert(status);
											alert(error); })
	;
}
