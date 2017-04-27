$(document).ready(function(){


  $('#form_addUser').submit(function(){
    console.log('submit working');
    var infoArr = [$('#first_name').val(), $('#last_name').val(), $('#email_address').val(), $('#contact_number').val()];
      if((infoArr.every(Boolean)) === true){
        var htmlContactInfoString = "<tr><td>"+infoArr[0]+"</td><td>"+infoArr[1]+"</td><td>"+infoArr[2]+"</td><td>"+infoArr[3]+"</td></tr>";
        console.log('true');
        $('form input[type=text]').val("");
      }
      else {
        alert("Fill in everything please! Don't be a jerk");
        console.log('false');
        //break;
      }
    $('#contact_info_table').append(htmlContactInfoString);
    return false;
  });

});
