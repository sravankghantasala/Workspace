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
		$.post( '/home/', { 'topic': topic } ).done ( function (data) {
			alert(JSON.stringify(data));
		} );
 };