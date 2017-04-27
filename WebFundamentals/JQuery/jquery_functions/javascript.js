$(document).ready(function(){

  $('#onClick button').click(function(){
    $('#onClick span').addClass("increase_font_size");
  });

  $('#hide button').click(function(){
    $('#hide span').hide();
  });

  $('#show button').click(function(){
    $('#show span').show();
  });

  $('#toggle button').click(function(){
    $('#toggle span').toggle(1000);
  });

  $('#slideDown button').click(function(){
    $('#slideDown span').slideDown(1000);
  });

  $('#slideUp button').click(function(){
    $('#slideUp span').slideUp(1000);
  });

  $('#slideToggle button').click(function(){
    $('#slideToggle span').slideToggle(1000);
  });

  $('#fadeIn button').click(function(){
    $('#fadeIn span').fadeIn(1000);
  });

  $('#fadeOut button').click(function(){
    $('#fadeOut span').fadeOut(1000);
  });

  $('#addClass button').click(function(){
    $('#addClass span').addClass('red font_family_change');
  });

  $('#before button').click(function(){
    $('#before span').before("<p>I'M ABOVE YOU! </p>");
  });

  $('#after button').click(function(){
    $('#after span').after("<p>I'M BELOW YOU! </p>");
  });

  $('#append button').click(function(){
    $('#append').append("<img src='https://ericsriley.files.wordpress.com/2012/11/i-need-hugs.jpg' alt='I NEED HUGS CAT!'>");
  });

  $('#html button').click(function(){
    $('#html span').html('THIS TEXT HAS CHANGED!');
  });

  $('#attr button').click(function(){
    $('#attr img').attr('src', 'https://pics.me.me/most-cats-look-down-at-you-questioning-your-intelligence-not-11008923.png');
  });

  $('#val button').click(function(){
    $('#val input').val('GOODBYE!');
  });

  $('#text button').click(function(){
    $('#text span').text('DID SOMETHING!');
  });

  $('#data button').click(function(){
    $('#data span').data('info', 'some_info');
  });

});
