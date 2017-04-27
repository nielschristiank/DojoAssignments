function insertPokemonImg(){

  for(var i = 1; i < 719; i++){
    var pokeImgHtmlString = '<img id="'+i+'" src="http://pokeapi.co/media/img/'+i+'.png">';
    $("#img_container").append(pokeImgHtmlString);
  }
}

// function getPokeData(){
//   for(var i = 1; i < 152; i++){
//     var pokeDataString = 'http://pokeapi.co/api/v1/pokemon/'+i+'/';
//   }
// }

function getPokeData(){
  $('img').hover(function(){
    // $('#info_box').show(500);
    var pokemon = this.id;
    $.get("http://pokeapi.co/api/v1/pokemon/"+pokemon+"/", function(res){
      console.log(res);
      var img = '<img src="http://pokeapi.co/media/img/'+pokemon+'.png">';
      var name = "<h1>"+res.name+"</h1>";
      var abilities = "<h4>Abilities</h4><ul>";
      for (var abil in res.abilities){
          abilities += "<li>"+res.abilities[abil].name+"</li>";
      }
      abilities += "</ul>";
      var types = "<h4>Types</h4><ul>";
      for (var type in res.types){
        types += "<li>"+res.types[type].name+"</li>";
      }
      types += "</ul>";
      var height = "<h4>Height</h4><ul><li>"+res.height+"</li></ul>";
      var weight = "<h4>Weight</h4><ul><li>"+res.weight+"</li></ul>";
      var infoHtmlString = img+name+abilities+types+height+weight;
      $('#info_box').html(infoHtmlString);
    }, "json");
  });
}

$(document).ready(function(){

  insertPokemonImg();

  getPokeData();

  $.get("http://pokeapi.co/api/v1/pokemon/30/", function(res){
    console.log(res);
  }, "json");

});
