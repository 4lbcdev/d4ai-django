$(document).ready(function() {
  var slides = $('.slider .slide');
  var currentIndex = 0;

  // Show the first slide initially
  slides.eq(currentIndex).addClass('active');

  // Automatically switch slides every 3 seconds
  setInterval(function() {
    slides.eq(currentIndex).removeClass('active').addClass('previous');

    // Remove the previous class from the previous slide
    slides.eq((currentIndex + slides.length - 1) % slides.length).removeClass('previous');

    // Add the next class to the next slide
    slides.eq((currentIndex + 1) % slides.length).addClass('next');

    // Slide out the previous slide to the right
    slides.eq(currentIndex).addClass('previous');

    // Slide in the next slide from the right
    slides.eq((currentIndex + 1) % slides.length).addClass('active').removeClass('next');

    // Increment the currentIndex
    currentIndex = (currentIndex + 1) % slides.length;
  }, 6000);
});



// $(document).ready(function() {

//   $('.nav').attr('src', './static/images/menu_open.png');
//   $('.drawer').hide();

//   // Click event handler for the image element
//   $('.nav').on('click', function() {
//     var $img = $(this);
//     var $drawer = $('.drawer');
    
//     // Check the current src value
//     if ($img.attr('src') === './static/images/menu_open.png') {
//       // Change the src to the new image
//       $img.attr('src', './static/images/menu_close.png');
//       $drawer.show();

//     } else {
//       // Change the src back to the original image
//       $img.attr('src', './static/images/menu_open.png');
//       $drawer.hide();
//     }
//   });
  
//   // Header scroll event handler
//   $(window).scroll(function() {
//     var scrollPosition = $(window).scrollTop();
//     var $header = $('header');
//     var $menuLinks = $('.menu a');

//     // Check the scroll position
//     if (scrollPosition >= 0) {
//       // Change the header background color to white
//       $header.css('background-color', 'white');
//       // Add the .header_border class to the header
//       $header.addClass('header_border');
//       // Change the color of menu links to black
//       $menuLinks.css('color', '#606060');

//     } else {
//       // Reset the header background color to transparent
//       $header.css('background-color', 'transparent');
//       // Remove the .header_border class from the header
//       $header.removeClass('header_border');
//       // Change the color of menu links to white
//       $menuLinks.css('color', 'white');
//     }
//   });

// });
