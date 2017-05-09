



$(document).ready(function() {

  $('img').click(function(){
    var house = $(this).attr('id');
    var houseUrl = "https://www.anapioficeandfire.com/api/houses/"+house+"/";
    $.get(houseUrl, function(res){
      console.log(res);
      var name = "<h1>"+res.name+"</h1>";
      var titles = "<h2>Titles</h2><ul>";
      for (var ttls in res.titles){
        titles += "<li>"+res.titles[ttls]+"</li>";
      }
      titles += "</ul>"
      var seats = "<h2>Seats</h2><ul>";
      for (var sts in res.seats){
        seats += "<li>"+res.seats[sts]+"</li>";
      }
      seats += "</ul>"
      var words = res.words;
      var swornMembers = "<h2>Sworn Members</h2><ul id='sMembers'>";
      for (var members in res.swornMembers)
        {
          $.get(res.swornMembers[members], function(resChar){
              swornMembers += "<li>"+resChar.name+"</li>";
            //  swornMembers += "</ul>";
              var htmlString = name+titles+seats+swornMembers;
              $('#info_box').html(htmlString);
            }, "json");
        }
        // var htmlString = name+titles+seats+swornMembers;
        // $('#info_box').html(htmlString);
    }, "json");
  });

});
// 362 378 229 17
