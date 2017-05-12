

function bracesValid(str)
{
  var arr = [];
  //var braces = {"}":"{","]":"[",")":"("};
  var braces = {"{":"}","[":"]","(":")"};
  for (var i = 0; i < str.length; i++)
  {
    if(str[i] === "{" || str[i] === "[" || str[i] === "(")
    {
        arr.push(str[i]);
    }
    else if(str[i] === "}" || str[i] === "]" || str[i] === ")")
    {
      if(arr.length === 0 || str[i] !== braces[arr[arr.length-1]])
      {
        return false;
      }
      else
      {
        arr.pop();
      }
    }
    else
    {
      continue;
    }
  }
  if(arr.length === 0)
  {
    return true;
  }
  else
  {
    return false;
  }
}
