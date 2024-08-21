$(document).ready(function () {
// ##############################  Cookie modal  #######################################
  // Function to get a cookie by name
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if this cookie's name matches the one we are looking for
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  // Function to set a cookie
  function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
  }

  // Function to handle the cookie notice display
  function handleCookieNotice() {
    var cookieAccepted = getCookie('cookie_accepted');

    if (cookieAccepted !== 'yes') {
        // Show the cookie notice after 4 seconds if not accepted
        setTimeout(function () {
            $('#cookie-notice').addClass('slide-up').css('bottom', '0px');
        }, 4000);
    }
  }

// Handle click event on the Accept button
$(document).on('click', '#cookie-notice .cn-button', function (e) {
  e.preventDefault(); // Prevent default action of the link
  setCookie('cookie_accepted', 'yes', 365); // Set cookie for 1 year
  $('#cookie-notice').hide(); // Hide the notice
});

// Initialize cookie notice handling
handleCookieNotice();

  // ##############################  Navigation  #######################################
  $('.menu-btn').change(function () {
    if ($(this).is(':checked')) {
      $('nav').css('display', 'flex');
    } else {
      $('nav').css('display', 'none');
    }
  });

  // ##############################  Messages PopUp #######################################
  let message = $('.popmessage');

  message.fadeIn(2000)
  setTimeout(() => {
    message.fadeOut(2000)
  }, 6000);

  // ##############################  Homepage - Vision Section Slider  #######################################
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

  // ##############################  Footer Subscribe Form  #######################################
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


