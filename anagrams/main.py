/** Directions
  Check to see if two provided strings are anagrams of eachother.
  One string is an anagram of another if it uses the same characters
  in the same quantity. Only consider characters, not spaces
  or punctuation.  Consider capital letters to be the same as lower case
  Examples
    anagrams('rail safety', 'fairy tales') => True
    anagrams('RAIL! SAFETY!', 'fairy tales') => True
    anagrams('Hi there', 'Bye there') => False
**/

def anagrams(str1, str2):
  clean_string(str1) == clean_string(str2)
  
def clean_string(str):
  x = ''.join(e for e in str if e.isalnum())
  x = x.lower()
  return ''.join(sorted(x))
