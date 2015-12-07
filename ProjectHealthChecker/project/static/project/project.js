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

//$( "#imageTestBtn" ).click(function() {
//  //alert( "Handler for .click() called." );
//  var csrftoken = getCookie('csrftoken');
//  $.ajax({
//        beforeSend: function(xhr, settings) {
//            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//                xhr.setRequestHeader("X-CSRFToken", csrftoken);
//            }
//        },
//        async: false,
//        url: '/project/imageTest/',
//        method: 'POST', // or another (GET), whatever you need
//        data: {
//            click: 'True'
//        },
//        dataType: "json",
//        success: function (data) {
//            //alert(data.status);
//            $( "#imageTestDisplay" ).empty();
//            if(data.status == 'success'){
//                $("#imageTestDisplay").append("<img src=\"/media/project/final.png\" class=\"img-responsive\">");
//            }else{
//                alert('Request Failed');
//            }
//        }
//    });
//});

$( "#imageTestBtn" ).click(function() {
    //alert("yes");
    location.reload();

});

$( "#evaluateBtn" ).click(function() {
  //alert( "Handler for .click() called." );
  var csrftoken = getCookie('csrftoken');
  projectCompletion = $( "#project_completion" ).val();
  spi = $( "#spi" ).val();
  cpi = $( "#cpi" ).val();
  developer_experience = $( "#developer_experience" ).val();
  task_completion = $( "#task_completion" ).val();
  test_cases_passed = $( "#test_cases_passed" ).val();
  $.ajax({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        async: false,
        url: '/project/form/',
        method: 'POST', // or another (GET), whatever you need
        data: {
            click: 'True',
            pr_cmp: projectCompletion,
            spi: spi,
            cpi: cpi,
            dev_exp: developer_experience,
            test_cases: test_cases_passed,
            task_cmplt: task_completion
        },
        dataType: "json",
        success: function (data) {
            alert(data.status);
//            $( "#imageTestDisplay" ).empty();
//            if(data.status == 'success'){
//                $("#imageTestDisplay").append("<img src=\"/static/project/final.png\" class=\"img-responsive\">");
//            }else{
//                alert('Request Failed');
//            }
        }
    });
});

$( "#submitInputBtn" ).click(function() {
  //alert( "Handler for .click() called." );
  var csrftoken = getCookie('csrftoken');
  projectId = $( "#projectList" ).find(":selected").val();
  projectCompletion = $( "#project_completion" ).val();
  spi = $( "#spi" ).val();
  cpi = $( "#cpi" ).val();
  developer_experience = $( "#developer_experience" ).val();
  task_completion = $( "#task_completion" ).val();
  test_cases_passed = $( "#test_cases_passed" ).val();
  $.ajax({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        async: false,
        url: '/project/current_input/',
        method: 'POST', // or another (GET), whatever you need
        data: {
            click: 'True',
            pr_id: projectId,
            pr_cmp: projectCompletion,
            spi: spi,
            cpi: cpi,
            dev_exp: developer_experience,
            test_cases: test_cases_passed,
            task_cmplt: task_completion
        },
        dataType: "json",
        success: function (data) {
            alert(data.status +"!! Press Ok to load SOM Visualization");
            //$( "#imageTestDisplay" ).empty();
            window.location = "/project/imageTest/";
//            if(data.status == 'success'){
//                window.location = "/project/imageTest/";
//            }else{
//                alert('Request Failed');
//            }
        }
    });
});