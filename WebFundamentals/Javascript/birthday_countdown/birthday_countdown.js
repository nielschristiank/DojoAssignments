function birthdayCountdown(days) {

  console.log(days + " days until birthday :(");
  while(days > 0)
  {
    days--;

    if(days > 30)
    {
      console.log(days + " days until birthday :(");
    }
    else if(days > 5)
    {
      console.log(days + " days until birthday :) yeah!");
    }
    else if(days <= 5 && days > 1)
    {
      console.log(days + " DAYS UNTIL YOUR BIRTHDAY!!!!!!!!");
    }
    else if(days === 1)
    {
      console.log(days + " DAY UNTIL YOUR BIRTHDAY!!!!!!!!");
    }
    else
    {
      console.log("IT'S YOUR BIRTHDAY!!!!!!!! TIME TO PARTY!!!!!");
    }
  }
}
birthdayCountdown(60);
