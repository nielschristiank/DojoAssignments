var _ = {
   map: function(arr, callback) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++){
      newArr.push(callback(arr[i]));
    }
    return newArr;
   },
   reduce: function(arr, callback, memo) {
     var start = 0;
     if(memo == undefined){
       memo = arr[0];
       start = 1;
     }
     for (var i = start; i < arr.length; i++){
       memo = callback(memo, arr[i]);
     }
     return memo;
   },
   find: function(arr, callback) {
     for (var i = 0; i < arr.length; i++){
       if (callback(arr[i])){
         return arr[i];
       }
     }
   },
   filter: function(arr, callback) {
     var newArr = [];
     for (var i = 0; i < arr.length; i++){
       if (callback(arr[i])){
         newArr.push(arr[i]);
       }
     }
     return newArr;
   },
   reject: function(arr, callback) {
     var newArr = [];
     for (var i = 0; i < arr.length; i++){
       if (!callback(arr[i])){
         newArr.push(arr[i]);
       }
     }
     return newArr;
   }
 }

console.log( _.map([1,2,3], function(num){ return num * 10; }));
console.log( _.reduce([1,2,3,4], function(memo, num){ return memo + num; }, 0));
console.log( _.reduce([1,2,3,4], function(memo, num){ return memo + num; }));
console.log(_.find([2,4,6,7,9], function(num){return num%2==1;}));
console.log(_.filter(["Kobe", "LeBron", "Steph", "Michael"], function(name){return name.length > 5;}));
var players = [{name: "Michael Jordan", rings:6},{name: "Kobe Bryant", rings:5},{name: "Lebron James", rings:3}]
console.log(_.reject(players, function(player){ return player.rings < 4; }));
