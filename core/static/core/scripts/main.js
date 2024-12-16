$(document).ready(function () {

  // #####  Navigation  #######################################
  $('.menu-btn').change(function () {
    if ($(this).is(':checked')) {
      $('nav').css('display', 'flex');
    } else {
      $('nav').css('display', 'none');
    }
  });

  // #####  Messages PopUp #######################################
  let message = $('.popmessage');

  message.fadeIn(2000)
  setTimeout(() => {
    message.fadeOut(2000)
  }, 6000);

  // #####  Homepage - Vision Section Slider  #######################################
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

  // #####  Read More Button  #######################################
  $('#about_more').hide();
  $('.read-more-button').click(function () {
    $('#about_more').fadeIn(3000);
    $('.read-more-button').hide();
  });

  // #####  Footer Subscribe Form  #######################################
  // Check if the email is valid
  function isValidEmail(email) {
    // Regular expression for email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  function checkInputs() {
    // const firstNameValue = $('#firstName').val().trim();
    // const lastNameValue = $('#lastName').val().trim();
    const emailValue = $('#email').val().trim();

    const isEmailValid = isValidEmail(emailValue);

    // Enable the button if all fields are filled, otherwise disable it
    $('#subscribeSubmitButton').prop('disabled', emailValue === '' || !isEmailValid);
  }
  // Add event listeners to input fields to check inputs whenever they change
  $('#email').on('input', checkInputs);
  checkInputs();
});


