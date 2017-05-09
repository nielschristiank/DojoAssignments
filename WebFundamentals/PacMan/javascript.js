
// List of Features to build
// 1) Have JS display the world of brick/coin/etc
// 2) Have the pacman move up and down

var world = [
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
  [2,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
  [2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,2],
  [2,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
  [2,1,2,1,2,1,2,1,2,1,2,2,2,2,2,2,2,2,1,2],
  [2,1,2,1,2,1,2,1,2,1,2,2,2,2,2,2,2,2,1,2],
  [2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2],
  [2,1,2,1,2,2,2,2,2,2,2,2,2,1,2,2,2,2,1,2],
  [2,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2],
  [2,1,2,1,2,1,2,2,2,2,2,0,2,1,2,1,2,2,1,2],
  [2,1,2,1,2,1,2,0,0,0,0,0,2,1,2,1,1,2,1,2],
  [2,1,2,1,2,1,2,2,2,2,2,2,2,1,2,2,2,2,1,2],
  [2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
  [2,1,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2],
  [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
  [2,1,2,2,2,1,2,2,2,2,2,2,2,2,1,2,2,2,1,2],
  [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
];

var pacman = {
  x: 1,
  y: 1
};

var ghost1 = {
  x: 8,
  y: 10
};

var score = 0;

function displayWorld(){
  var output = "";

  for(var i = 0; i < world.length; i++){
    output += "<div class='row'>";
    for(var j = 0; j < world[i].length; j++){
      if(world[i][j] == 2){
        output += "<div class='brick'></div>";
      }
      else if(world[i][j] == 1){
        output += "<div class='coin'></div>";
      }
      else if(world[i][j] == 0){
        output += "<div class='empty'></div>";
      }
    }
    output += "</div>";
  }
  document.getElementById('world').innerHTML = output;
}

function displayPacman(){
  document.getElementById('pacman').style.top = pacman.y*20+"px";
  document.getElementById('pacman').style.left = pacman.x*20+"px";
}

function displayGhosts(){
  document.getElementById('ghost1').style.top = ghost1.y*20+"px";
  document.getElementById('ghost1').style.left = ghost1.x*20+"px";
}

// function displayMoveGhost(){
//   document.getElementById('ghost1').style.top = ghost1.y*20+"px";
//   document.getElementById('ghost1').style.left = ghost1.x*20+"px";
// }

function displayScore(){
  document.getElementById('score').innerHTML = score;
}

// function moveGhosts(){
//     while(world[ghost1.y][ghost1.x-1] == 2){
//       ghost1.x++;
//       displayGhosts();
//     }
//     while(world[ghost1.y][ghost1.x-1] !=2 && world[ghost1.y][ghost1.x+1] != 2) {
//       ghost1.x--;
//       //setInterval(displayGhosts, 1000);
//       displayGhosts();
//     }
//     while(world[ghost1.y+1][ghost1.x] != 2){
//       ghost1.y++;
//       //setInterval(displayGhosts, 1000);
//       displayGhosts();
//     }
//     while(world[ghost1.y-1][ghost1.x] != 2){
//       ghost1.y--;
//       //setInterval(displayGhosts, 1000);
//       displayGhosts();
//     }
//   }
function moveGhosts(){
    if(world[ghost1.y][ghost1.x+1] != 2){
      ghost1.x++;
      displayGhosts();
    }
    if(world[ghost1.y-1][ghost1.x] != 2) {
      ghost1.y--;
      //setInterval(displayGhosts, 1000);
      displayGhosts();
    }
    // if(world[ghost1.y+1][ghost1.x] != 2 && world[ghost1.y][ghost1.x+1] == 2){
    //   ghost1.y++;
    //   //setInterval(displayGhosts, 1000);
    //   displayGhosts();
    // }
    // else if(world[ghost1.y-1][ghost1.x] != 2){
    //   ghost1.y--;
    //   //setInterval(displayGhosts, 1000);
    //   displayGhosts();
    // }
}
// function moveGhosts(){
//     if(world[ghost1.y][ghost1.x+1] != 2){
//       ghost1.x++;
//       displayGhosts();
//     }
//     else if(world[ghost1.y][ghost1.x-1] !=2) {
//       ghost1.x--;
//       //setInterval(displayGhosts, 1000);
//       displayGhosts();
//     }
//     if(world[ghost1.y+1][ghost1.x] != 2){
//       ghost1.y++;
//       //setInterval(displayGhosts, 1000);
//       displayGhosts();
//     }
//     else if(world[ghost1.y-1][ghost1.x] != 2){
//       ghost1.y--;
//       //setInterval(displayGhosts, 1000);
//       displayGhosts();
//     }
// }

document.onkeydown = function(e){
  if(e.keyCode == 37 && world[pacman.y][pacman.x-1] != 2){ //left
    pacman.x--;

  }
  else if(e.keyCode == 39 && world[pacman.y][pacman.x+1] != 2){ //right
    pacman.x++;
  }
  else if(e.keyCode == 38 && world[pacman.y-1][pacman.x] != 2){ //up
    pacman.y--;
  }
  else if(e.keyCode == 40 && world[pacman.y+1][pacman.x] != 2){ //down
    pacman.y++;
  }
  if(world[pacman.y][pacman.x] == 1){
    world[pacman.y][pacman.x] = 0;
    score += 10;
    displayScore();
    displayWorld();
  }
//  console.log(e.keyCode);
  displayPacman();
}
