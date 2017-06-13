var math_module = require('./mathlib.js');
math = math_module();

console.log(math.add(2,3));
console.log(math.multiply(2,3));
console.log(math.square(3));
console.log(math.random(10,1));
