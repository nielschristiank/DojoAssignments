function VehicleConstructor(name, wheels, passengers){

  var vehicle = {};

  vehicle.name = name;
  vehicle.wheels = wheels;
  vehicle.passengers = passengers;

  vehicle.makeNoise = function(){
    console.log("VROOM VROOM! BEEP BEEP!")
  }
  return vehicle;
}

var Bike = VehicleConstructor("Bike", 2, 1);
console.log(Bike);
Bike.makeNoise();
Bike.makeNoise = function() {console.log("ring ring");}
Bike.makeNoise();

var Sedan = VehicleConstructor("Sedan", 4, 5);
console.log(Sedan);
Sedan.makeNoise();
Sedan.makeNoise = function() {console.log("Honk! Honk!");}
Sedan.makeNoise();

var Bus = VehicleConstructor("Bus", 8, 1);
console.log(Bus);
Bus.pickUpPassenger = function(passengers){Bus.passengers += 1;}
Bus.pickUpPassenger();
console.log(Bus);
