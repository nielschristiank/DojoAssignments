

function commonSuffix(arr)
{
  var newArr = [];
  var result = "";
  for (var i = 1; i < arr[0].length + 1; i++)
  {
    for (var j = 1; j < arr.length; j++)
    {
      if (arr[0][arr[0].length - i] != arr[j][arr[j].length - i])
      {
        break;
      }
      else if (j == arr.length - 1)
      {
        newArr.push(arr[0][arr[0].length - i])
      }
    }
  }
  for (var char = (newArr.length - 1); char >= 0; char--)
  {
    result += newArr[char];
  }
  return result;
}
