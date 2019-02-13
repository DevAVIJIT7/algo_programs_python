/**
  Directions
    Write a function that accepts a string.  The function should
    capitalize the first letter of each word in the string then
    return the capitalized string.
    Examples
      capitalize('a short sentence') => 'A Short Sentence'
      capitalize('a lazy fox') => 'A Lazy Fox'
      capitalize('look, it is working!') => 'Look, It Is Working!'
**/

def capitalize(str):
  result = str[0].upper()
  for i in range(1, len(str)):
    if str[i-1] == ' ':
      result += str[i].upper()
    else:
      result += str[i]
      
  return result
