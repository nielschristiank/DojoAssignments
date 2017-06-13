
function personConstructor(name){

  var person = {
    name: name,
    distance_traveled: 0,
    say_name: function(){
      console.log(this.name);
      return this;
    },
    say_something: function(something){
      console.log(`${person.name} says: ${something}`)
      return this;
    },
    walk: function() {
      console.log(`${this.name} is walking`);
      this.distance_traveled += 3;
      return this;
    },
    run: function() {
      console.log(`${this.name} is running`);
      this.distance_traveled += 10;
      return this;
    },
    crawl: function() {
      console.log(`${this.name} is crawling`);
      this.distance_traveled += 1;
      return this;
    },
  }

  return person;
};

function ninjaConstructor(name, cohort){

    var ninja = {};
    var belts = ["yellow belt", "red belt", "black belt"];
    ninja.name = name;
    ninja.cohort = cohort;
    ninja.belt_level = 0;
    ninja.level_up = function(){
      if (ninja.belt_level < 2){
          ninja.belt_level += 1;
          ninja.belt = belts[ninja.belt_level];
        };
        return ninja;
      };
    ninja.belt = belts[ninja.belt_level];
    return ninja;
}

var Bob = personConstructor('Bob');
Bob.say_name().say_something('Yo yo');

var ninja = ninjaConstructor("Sue", "MEAN");
console.log(ninja.name);
console.log(ninja.belt);
ninja.level_up();
console.log(ninja.belt);
