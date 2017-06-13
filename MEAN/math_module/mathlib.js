module.exports = function (){
  return {
    // adds two numbers
    add: function(num1, num2) {
      return num1 + num2;
    },
    // mult two numbers
    multiply: function(num1, num2){
      return num1 * num2;
    },
    // square number
    square: function(num){
      return num * num;
    },
    // return random number between 2 values
    random: function(num1, num2){
      if(num2 > num1){
        return Math.round(Math.random()*(num2-num1)) + num1;
      }
      else{
        return Math.round(Math.random()*(num1-num2)) + num2;
      }
    }
  }
};
