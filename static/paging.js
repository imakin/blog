$( document ).ready(function() {

	$(window).scroll(function () {
		var scrollpos = $(window).scrollTop();
		
		document.getElementById("scroll").innerHTML=scrollpos;
	});


});
