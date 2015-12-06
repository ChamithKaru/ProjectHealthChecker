function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$( "#imageTestBtn" ).click(function() {
  //alert( "Handler for .click() called." );
  var csrftoken = getCookie('csrftoken');
  $.ajax({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        async: false,
        url: '/project/imageTest/',
        method: 'POST', // or another (GET), whatever you need
        data: {
            click: 'True'
        },
        dataType: "json",
        success: function (data) {
            //alert(data.status);
            $( "#imageTestDisplay" ).empty();
            if(data.status == 'success'){
                $("#imageTestDisplay").append("<img src=\"/static/project/final.png\" class=\"img-responsive\">");
            }else{
                alert('Request Failed');
            }
        }
    });
});