(function ($) {
	"use strict";

	// Initiate the wowjs animation library
	new WOW().init();


	// Back to top button
	$(window).scroll(function() {
		if ($(this).scrollTop() > 100) {
	    	$('.back-to-top').fadeIn('slow');
	  	} else {
	    	$('.back-to-top').fadeOut('slow');
	  	}
	});

	$('.back-to-top').click(function(){
	  	$('html, body').animate({scrollTop : 0},1500, 'easeInOutExpo');
	  	return false;
	});

  	// Wedding Party carousel (uses the Owl Carousel library)
	$('.owl-carousel').owlCarousel({
		autoplay: true,
	    loop:true,
	    margin:10,
	    responsiveClass:true,
	    responsive: { 0: { items: 1 }, 768: { items: 3 }, 900: { items: 4 }}
	})

	


})(jQuery);

