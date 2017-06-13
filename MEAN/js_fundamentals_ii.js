function sum(x, y){
  var sum = 0;
  for (x; x <=y; x++){
    sum += x;
  }
  console.log(sum);
}

function findMin(arr){
  var min = arr[0];
  for (var i = 0; i < arr.length; i++){
    if(min > arr[i]){
      min = arr[i];
    }
  }
  return min;
}

function findAvg(arr){
  var sum = 0;
  for(var i = 0; i < arr.length; i++){
    sum += arr[i];
  };
  return (sum/arr.length);
}

var person = {
  name: 'Niels-Christian',
  distance_traveled: 0,
  say_name: function(){
    console.log(person.name);
    return person;
  },
  say_something: function(something){
    console.log('${person.name} says: ${something}')
  },
  walk: function() {
    console.log(`${person.name} is walking`);
    person.distance_traveled += 3;
    return person;
  },
  run: function() {
    console.log(`${person.name} is running`);
    person.distance_traveled += 10;
    return person;
  },
  crawl: function() {
    console.log(`${person.name} is crawling`);
    person.distance_traveled += 1;
    return person;
  },
}

person.say_name().walk().crawl()
