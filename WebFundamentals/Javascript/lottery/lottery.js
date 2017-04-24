function lottery(q) {

  var win = Math.floor((Math.random() * 100) + 1);

  while (q > 0){
    var chance = Math.floor((Math.random() * 100) + 1);
    if(chance === win){
      return Math.floor((Math.random() * 50) + 51);
    }
    q--;
  }
  return "Out of quarters";
}
