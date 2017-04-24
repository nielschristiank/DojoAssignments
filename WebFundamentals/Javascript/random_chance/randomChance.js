function lottery(coins, limit, winAmount){

  var win = Math.floor(Math.random() * 100) + 1;

  for(var i = coins; i > 0; i--){
    var chance = Math.floor(Math.random() * 100) + 1;
    if(chance === win){
      var winnings = (Math.floor(Math.random() * 50) + 50);

      return "You won: " + winnings + " You have: " + i +" quarters left";
    }
  }
  return "you are out of quarters"
}


function lottery2(coins, winAmount){

  var win = Math.floor(Math.random() * 100) + 1;
  var winnings = 0;

  while(winnings < winAmount && coins > 0){
  //  for(var i = coins; i >= 0; i--){
      var chance = Math.floor(Math.random() * 100) + 1;
      if(chance === win){
        var winnings = winnings + (Math.floor(Math.random() * 50) + 50);
      //  return "You won: " + winnings + " You have: " + i +" quarters left";
      }
    //}
    coins--;
  }
  return "You have won " + winnings + " quarters and have " + coins + " quarters left.";
}
