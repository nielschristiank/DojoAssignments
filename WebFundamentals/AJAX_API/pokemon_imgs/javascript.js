function insertPokemon(){

  for(var i = 1; i < 719; i++){
    var pokeImgString = '<img src="http://pokeapi.co/media/img/'+i+'.png">';
    $("#main_container").append(pokeImgString);
  }
}


$(document).ready(function(){

  insertPokemon();

});
