$(document).ready(function(){

  $('img').click(function(){
    $(this).hide(1000);
  })

  $('button').click(function(){
    $('img').show(1000);
  });

});
