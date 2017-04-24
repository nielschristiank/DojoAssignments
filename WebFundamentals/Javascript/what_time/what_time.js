function whatTime(hr, min, am_pm){

  var intro = " ";
  var outro = " ";

  if(min >= 30)
  {
    hr += 1;
    intro = "It is almost ";
  }
  else
  {
    intro = "It's just after ";
  }
  if(am_pm === "AM")
  {
    outro = " in the morning";
  }
  else
  {
    outro = " in the evening";
  }
  console.log(intro+hr+outro);
}


function whatTime(hr, min, am_pm){

  var message = "";

  if(min >= 30)
  {
    message += "It is almost " + (hr+1);
  }
  else
  {
    message += "It's just after " + hr;
  }
  if(am_pm === "AM")
  {
    message += " in the morning";
  }
  else
  {
    message += " in the evening";
  }
  console.log(message);
}
