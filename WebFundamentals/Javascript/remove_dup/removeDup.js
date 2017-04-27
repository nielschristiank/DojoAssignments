function removeDup(arr) //long version
{
  for(var i = 0; i < arr.length - 1; i++)
  {
    if(arr[i] === arr[i+1])
    {
      for(var j = i; j < arr.length - 1; j++)
      {
        arr[j] = arr[j+1];
      }
      arr.length = arr.length - 1;
                //arr.pop(arr.length - 1);
      i--;
    }
  }
  return arr;
}


function removeDup2(arr)
{
  for (var i = 0; i < arr.length; i++)
  {
    var count = 0;
    var j = i+1;
    while(arr[i] === arr[j])
    {
      j++;
      count++;
    }
    if(count>0)
     {
      var x = i;
      for (j; j < arr.length; j++)
      {
        arr[++x] = arr[j];
      }
      arr.length = arr.length - count;
     }
  }
  return arr;
}

function removeDupUnsorted(arr)
{
  for(var i = 0; i < arr.length; i++)
  {
    for(var j = i+1; j < arr.length; j++)
    {
      if(arr[i] === arr[j])
      {
        for(j; j < arr.length - 1; j++)
        {
          arr[j] = arr[j+1];
        }
        arr.length = arr.length - 1;
        i--;
      }
    }
  }
  return arr;
}
