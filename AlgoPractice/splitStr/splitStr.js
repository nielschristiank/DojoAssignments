
/*** STRING SPLIT ***/
function splitStr(str, delim, lim){

  if (lim === undefined)
  {
    lim = str.length;
  }
  var arr = [];
  tempStr = "";

  for(var i = 0; i < str.length; i++)
  {
    if(str[i] !== delim[0] && arr.length < lim)
    {
      tempStr += str[i];
    }
    else if (str[i] === delim[0])
    {
      dStr = "";
      for (var j = 0; j < delim.length; j++)
      {
        dStr += delim[j];
      }
      if (dStr === delim)
      {
        i += delim.length-1;
        arr.push(tempStr);
        tempStr = "";
        continue;
      }
    }
  }
  if (tempStr !== "")
  {
    arr.push(tempStr);
  }
  return arr;
}

/*** STRING SEARCH ***/
function searchStr(str, val)
{
  var count = 0;
  for (var i = 0; i < str.length; i++)
  {
      if(str[i] === val[0])
      {
        vStr = "";
        for(var j = 0; j < val.length; j++)
        {
          vStr += str[i+j];
        }
        if (vStr == val)
        {
          return i;
        }
      }
  }
  return -1;
}

/*** STRING SEARCH, RETURN ARRAY OF ALL INDICES ***/

function searchStrAll(str, val)
{
  var arr = [];
  var count = 0;
  for (var i = 0; i < str.length; i++)
  {
      if(str[i] === val[0])
      {
        vStr = "";
        //console.log(vStr);
        for(var j = 0; j < val.length; j++)
        {
          vStr += str[j+i];
          //console.log(vStr);
        }
        if (vStr === val)
        {
          count++;
          //console.log(count);
          arr.push(i);
          i += vStr.length - 1;
        }
        else if (vStr !== val)
        {
          continue;
        }
      }
  }
   if(count === 0)
   {
     return -1;
   }
   else
   {
     return arr;
   }
}
