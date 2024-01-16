$(document).ready(function () {

// ##############################  Cookie modal  #######################################
  var cookieNotice = document.getElementById('cookie-notice');
  if (cookieNotice) {
      setTimeout(function () {
          cookieNotice.classList.add('slide-up');
          cookieNotice.style.bottom = '0px';
      }, 4000);
  }

  // Event handler for the "Accept" button
  $(".cn-button").on("click", function (e) {
      e.preventDefault();
      cookieNotice.style.display = 'none';
  });

// ##############################  Navigation  #######################################
  $('.menu-btn').change(function () {
    if ($(this).is(':checked')) {
      $('nav').css('display', 'flex');
    } else {
      $('nav').css('display', 'none');
    }
  });

// ##############################  Messages  #######################################
  let message = $('.popmessage');

  message.fadeIn(2000)
  setTimeout(() => {
    message.fadeOut(2000)
  }, 6000);

// ##############################  Homepage Vision Slider  #######################################
  var slides = $('.slider .slide');
  var currentIndex = 0;

  // Show the first slide initially
  slides.eq(currentIndex).addClass('active');

  // Automatically switch slides every 3 seconds
  setInterval(function () {
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

// ##############################  Read More Button  #######################################
  $('#about_more').hide();
  $('.read-more-button').click(function () {
    $('#about_more').fadeIn(3000);
    $('.read-more-button').hide();
  });
});


