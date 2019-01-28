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

  	// Wedding Party carousel (uses the Slick library)
	$('.weddingparty-carousel').slick({
		slidesToShow: 5,
  		slidesToScroll: 1,
  		autoplay: true,
  		autoplaySpeed: 2000,
        dots: true,
  		infinite: true,
  		responsive: [
  		    {
  		      breakpoint: 1024,
  		      settings: {
  		        slidesToShow: 5
  		      }
  		    },
  		    {
  		      breakpoint: 768,
  		      settings: {
  		        slidesToShow: 3
  		      }
  		    },
  		    {
  		      breakpoint: 480,
  		      settings: {
  		        slidesToShow: 1
  		      }
  		    }
  		  ]
      });

})(jQuery);

