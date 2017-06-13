function VehicleConstructor(name, wheels, passengers, speed){
  if (!(this instanceof VehicleConstructor)){
   return new VehicleConstructor(name,wheels,passengerNumber, speed);
 }
  var chars = "0123456789ABCEDGHIJKLMNOPQRSTUVWXYZ";
  this.name = name;
  this.wheels = wheels;
  this.passengers = passengers;
  this.speed = speed;
  this.distance_traveled = 0;
  this.vin = createVin();
  function createVin(){
    var vin = "";
    for (var i = 0; i < 17; i++){
      vin += chars[Math.floor(Math.random()*35)];
    }
    return vin;
  }
  return this;
}

VehicleConstructor.prototype.makeNoise = function(){
  console.log("VROOM VROOM! BEEP BEEP!");
  return this;
}

VehicleConstructor.prototype.move = function(){
  this.makeNoise();
  this.distance_traveled += this.speed;
  console.log(this.distance_traveled)
}

VehicleConstructor.prototype.checkMiles = function(){
  console.log(this.distance_traveled);
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
