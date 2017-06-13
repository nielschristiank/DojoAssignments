var x = [3,5,"Dojo", "rocks", "Michael", "Sensei"];
x.push(100);
for (var i = 0; i < x.length; i++){
  console.log(x[i]);
}

var x = ["hello", "world", "JavaScript is fun"];
console.log(x);



var newNinja = {
  name: 'Jessica',
  profession: 'coder',
  favorite_language: 'JavaScript',
  dojo: 'Dallas'
};

for (var key in newNinja){
  console.log(key, newNinja[key])
};

var sum = 0;
for (var i = 1; i <= 500; i++){
  sum += i;
}
console.log(sum);

var arr = [1,5,90,25,-3,0];
var min = arr[0];
for (var i = 0; i < arr.length; i++){
    if (min > arr[i]){
      min = arr[i];
    }
}
console.log(min)

var arr = [1,5,90,25,-3,0];
var sum = 0;
for (var i = 0; i < arr.length; i++){
    sum += arr[i];
}

console.log(sum/arr.length);
