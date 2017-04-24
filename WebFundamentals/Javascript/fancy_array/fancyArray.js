function fancyArray(){
  var arr = ["James", "Jill", "Jane","Jack"];

  for (var i = 0; i < arr.length; i++){
    console.log(i+" -> "+arr[i]);
  }
}

function fancyArrayWithSym(symbol){
  var arr = ["James", "Jill", "Jane","Jack"];

  for (var i = 0; i < arr.length; i++){
    console.log(i+" "+symbol+" "+arr[i]);
  }
}

function fancyArrWithSymRev(symbol, reversed){
  var arr = ["James", "Jill", "Jane","Jack"];

  if(reversed === true){
    for (var i = arr.length - 1; i >= 0; i--){
      console.log(i+" "+symbol+" "+arr[i]);
    }
  }
  else {
    for (var i = 0; i < arr.length; i++){
      console.log(i+" "+symbol+" "+arr[i]);
    }
  }
}
