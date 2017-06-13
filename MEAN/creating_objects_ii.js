function VehicleConstructor(name, wheels, passengers, speed){

  if (!(this instanceof VehicleConstructor)){
   return new VehicleConstructor(name,wheels,passengerNumber, speed);
 }

  var self = this;
  var distance_traveled = 0;
  var updateDistance = function(){
    distance_traveled += self.speed;
    console.log(distance_traveled)
  }
  this.name = name;
  this.wheels = wheels;
  this.passengers = passengers;
  this.speed = speed;
  this.makeNoise = function(){
    console.log("VROOM VROOM! BEEP BEEP!");
  }
  this.move = function(){
    this.makeNoise();
    updateDistance();
  }
  this.checkMiles = function(){console.log(this.distance_traveled);}
}

var Bike = new VehicleConstructor("Bike", 2, 1, 15);
console.log(Bike);
Bike.makeNoise();
Bike.makeNoise = function() {console.log("Ring! Ring!");}
Bike.makeNoise();
Bike.checkMiles();
Bike.move();
Bike.checkMiles();

var Sedan = new VehicleConstructor("Sedan", 4, 5, 70);
console.log(Sedan);
Sedan.makeNoise();
Sedan.makeNoise = function() {console.log("Honk! Honk!");}
Sedan.makeNoise();

var Bus = new VehicleConstructor("Bus", 8, 1, 55);
console.log(Bus);
Bus.pickUpPassenger = function(passengers){Bus.passengers += 1;}
Bus.pickUpPassenger();
console.log(Bus);
