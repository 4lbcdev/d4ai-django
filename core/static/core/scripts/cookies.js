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
});
    
    
    