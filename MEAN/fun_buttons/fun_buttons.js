
$(document).on('click', 'button', function(){
	$(this).toggleClass("red");
});


$("button").hover(function(){
	$(this).addClass("green")
}, function(){ $(this).removeClass("green") });
