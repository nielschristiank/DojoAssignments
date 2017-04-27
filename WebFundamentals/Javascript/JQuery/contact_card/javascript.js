//
// function attach_contact_handlers(){
//   $(".contact p").click(function(){
//     $(this).siblings('p.hidden').slideToggle(500);
//     //$(this).text('Click again to hide');
//   });
// }

$(document).ready(function(){

 // attach_contact_handlers();

  // $("#contact p").click(function(){
  //   $(this).siblings('p.hidden').slideToggle(500);
  //   //$(this).text('Click again to hide');
  //   attach_contact_handlers();
  // });

  // $(document).on("click", ".contact p", function(){
  // //  $("#contact p").click(function(){
  //     $(this).siblings('p.hidden').slideToggle(500);
  //   });

    $(document).on("click", ".contact", function(){
    //  $("#contact p").click(function(){
        $(this).children('p, h1').slideToggle(500);
    });

      // $(document).on("click", ".contact p", function(){
      // //  $("#contact p").click(function(){
      //     $(this).siblings('p.hidden').slideToggle(500);
      //   });

  $('#form_addUser').submit(function(){
    var userInfoArr = [$('#first_name').val(), $('#last_name').val(), $('#description').val()];
//    if((userInfoArr.every(Boolean)) === true){
      var userInfoHtmlString = '<div class="contact"><h1>'+userInfoArr[0]+' '+userInfoArr[1]+'</h1><p>Click for description</p><p class="hidden">'+userInfoArr[2]+'</p></div>';
      $('form input[type=text], form textarea').val("");
//     }
// //    else {
//       alert("please fill out everything");
//     }
    $('#contact_container').append(userInfoHtmlString);
    // attach_contact_handlers();
    return false;
  });


});
