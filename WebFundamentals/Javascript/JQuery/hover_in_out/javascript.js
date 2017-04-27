$(document).ready(function(){

  $('img').hover(function()
  {
    var ninja = $(this).attr('src');
    var cat = $(this).attr('data-alt-src');
    $(this).attr('src', cat);
    $(this).attr('data-alt-src', ninja);
  });


});
