function forAFewBillion(days) {

  var sum = 0;

  for(var i = 0; i < days; i++) {
    sum = sum + (Math.pow(2,i))*0.01;
  }
  console.log(sum +" "+ i);
}


function forAFewBillionMore(amount) {

  var sum = 0;
  for(var i = 0; sum <= amount; i++) {
    sum = sum + (Math.pow(2,i))*0.01;
  }
  console.log("You made: $" + sum +" in "+ i + " days");
}
