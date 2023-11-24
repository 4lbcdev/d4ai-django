$(document).ready(function() {
    
  $('#nav').attr('src', "{% static 'core/images/menu_open.png' %}");
  
  // Click event handler for the image element
  $('#nav').on('click', function() {
      var $img = $(this);
      var $drawer = $('.drawer');
      
      // Check the current src value
      if ($img.attr('src') === "{% static 'core/images/menu_open.png' %}") {
      // Change the src to the new image
      $img.attr('src', "{% static 'core/images/menu_close.png' %}");
      $drawer.css('display', 'flex');
      $drawer.css('display', '-webkit-flex');
      $drawer.css('display', '-ms-flexbox');
      // $drawer.show();
  
      } else {
      // Change the src back to the original image
      $img.attr('src', "{% static 'core/images/menu_open.png' %}");
      $drawer.css('display', 'none');
      }
  });

  let message = $('.popmessage');
  
  $(document).ready(function(){
      message.fadeIn(2000)
      setTimeout(()=>{
          message.fadeOut(2000)
      },6000)
      
      // Check Radio-box
      $(".rating input:radio").attr("checked", false);
      
      $('.rating input').click(function () {
          $(".rating span").removeClass('checked');
          $(this).parent().addClass('checked');
      });
  });
});


// Homepage Vision Slider

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


// Homepage Read more button

$(document).ready(function() {
  $('#about_more').hide();
  $('.read-more-button').click(function() {
      $('#about_more').fadeIn(3000);
      $('.read-more-button').hide();
  });
});