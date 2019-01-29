(function ($) {
	"use strict";


	// Initiate the wowjs animation library
	new WOW().init();

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

