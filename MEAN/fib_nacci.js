function fib(){
  var fibNum = 0;
  var nacciNum = 1;
  function nacci(){
    console.log(nacciNum);
    var temp = fibNum;
    fibNum = nacciNum;
    nacciNum = temp + nacciNum;
  }
  return nacci;
}

var counter = fib();
counter();
counter();
counter();
counter();
counter();
counter();
counter();
counter();
counter();
counter();
counter(); //89
counter(); 
