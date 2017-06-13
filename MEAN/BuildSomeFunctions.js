
function runningLogger(){
  console.log("I am running!");
};

function multiplyByTen(num){
  num *= 10;
  return num;
};

function stringReturnOne(){
  return "String One";
};

function stringReturnTwo(){
  return "String Two";
};

function caller(func){
  if (typeof(func) == 'function'){
    func;
  };
};

function myDoubleConsoleLog(func1, func2){
  if (typeof (func1) === 'function' && typeof(func2) === 'function'){
    console.log(func1(), func2());
  };
};

function caller2(func){
  console.log(typeof(func));
  if (typeof(func) === 'function'){
    console.log('starting')
    setTimeout(func(), 2000);
    console.log('ending?','interesting')
  };
};


caller2(myDoubleConsoleLog(stringReturnOne,stringReturnTwo));
