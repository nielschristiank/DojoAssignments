$(document).ready(function(){

  $('img').click(function(){
    var ninja = $(this).attr('src');
    var cat = $(this).attr('data-alt-src');
    $(this).attr('src', cat);
    $(this).attr('data-alt-src', ninja);
  });



});
