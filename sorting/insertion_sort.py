/**
  Program use for sorting array using insertion sort.
  Write a method for moving array elements next position
  if elements are greater than the given value.
  Then call these methods while looping through array elements.
**/

def insert(array, right_index, value):
    i = right_index
    while(i >= 0 and array[i] > value):
        array[i+1] = array[i]
        i = i - 1
    
    array[i+1] = value

def insertion_sort(array):
    for j in range(len(array)):
        insert(array, j - 1, array[j])
    
    return array
array = [22, 11, 99, 88, 9, 7, 42]
print(insertion_sort(array) == [7, 9, 11, 22, 42, 88, 99])
