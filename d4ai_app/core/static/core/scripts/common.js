$(document).ready(function() {

    $('#nav').attr('src', './static/images/menu_open.png');
    // $('.drawer').hide();
  
    // Click event handler for the image element
    $('#nav').on('click', function() {
      var $img = $(this);
      var $drawer = $('.drawer');
      
      // Check the current src value
      if ($img.attr('src') === './static/images/menu_open.png') {
        // Change the src to the new image
        $img.attr('src', './static/images/menu_close.png');
        $drawer.css('display', 'flex');
        $drawer.css('display', '-webkit-flex');
        $drawer.css('display', '-ms-flexbox');
        // $drawer.show();
  
      } else {
        // Change the src back to the original image
        $img.attr('src', './static/images/menu_open.png');
        $drawer.css('display', 'none');
        // $drawer.hide();
      }
    });  
  });
  