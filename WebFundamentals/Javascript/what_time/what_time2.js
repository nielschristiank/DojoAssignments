function whatTime(hr, min, am_pm) {

  var intro = "";
  var outro = "";

  if (min < 30) {
    if (min < 5) {
      intro = "It is almost five past ";
    }
    if (min === 5) {
      intro = "It is five past ";
    }
    if (15 > min > 5) {
      intro = "It is almost quart past ";
    }
    if (min === 15){
      intro = "It is quarter past ";
    }
    if (30 > min > 15) {
      intro = "It is almost half past ";
    }
    if (min === 30) {
      intro = "It is half past ";
    }
  }
  else {
    hr += 1;
    if (30 < min < 45) {
      intro = "It is almost quarter to ";
    }
    if (min === 45) {
      intro = "It is quarter to ";
    }
    else if (min > 45){
      intro = "It is almost ";
    }
  }

  if(am_pm === "AM"){
    if(5 < hr < 12) {
      outro = " in the morning";
    }
    if (hr === 12 && min === 0) {
      intro = "It is noon ";
      hr ="";
      outro = "";
    }
    else if (5 < hr < 12){
      outro = " at night";
    }
  }
  if(am_pm === "PM") {
    if(12 < hr < 5) {
      outro = " in the afternoon";
    }
    if( hr === 12 && min === 0){
      intro = "It is midnight";
      hr = "";
      outro = "";
    }
    else if(5 < hr < 12){
      outro = " in the evening"
    }
  }
  console.log(intro+hr+outro);
}


























  if(min < 5){
    intro = "It is almost five after ";
  }
  if(min === 5){
    intro = "It is five after ";
  }
  if(5 < min < 15){
    intro = "It is almost quarter after ";
  }
  if(min === 15){
    intro = "It is quarter past ";
  }
  if(15 < min < 30) {
    intro = "It is almost half past ";
  }
  if(min === 30){
    intro = "It is half past ";
  }
  if(30 < min < 45){
    hr+=1;
    intro = "It is almost quarter to ";
  }
  if(min === 45){
    hr += 1;
    intro = "It is quarter to ";
  }
  else{
    intro = "It is almost ";
  }
  if(hr === 12 && min === 0 && am_pm === "PM"){
    intro = "It is noon ";
    outro = " ";
    hr = " ";
  }
  if(am_pm === "AM" && hr > 6){
    outro = " in the morning";
  }
  if(am_pm === "PM" && hr < 5){
    outro = " in the afternoon"
  }
  if(am_pm === "PM" && hr >= 5){
    outro = " in the evening";
  }
  else{
    outro = " at night";
  }
  console.log(intro+hr+outro);
}
