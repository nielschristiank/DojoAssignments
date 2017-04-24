function removeDup(arr)
{
  for(var i = 0; i < arr.length - 1; i++)
  {
    if(arr[i] === arr[i+1])
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
