function numbersOnly(arr)
{
  var newArr = [];
  for(var i = 0; i < arr.length; i++)
  {
    if (typeof arr[i] == "number")
    {
      newArr.push(arr[i]);
    }
  }
  return newArr;
}

function numbersOnly2(arr)
{
  for(var i = 0; i < arr.length; i++)
  {
    if (typeof arr[i] != "number")
    {
      for(var j = i; j < arr.length - 1; j++)
      {
        arr[j] = arr[j+1];
      }
      arr.pop(arr.length - 1);
      i--;
    }
  }
  return arr;
}
