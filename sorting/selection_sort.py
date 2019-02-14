/**
  Program use for sorting array using selection sort.
  Write two method for swapping and find minimum value
  of a array.Then call these methods while looping
  through array elements.
**/

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def find_min_index(array, start_index):
    min_value = array[start_index]
    min_index = start_index
    i = min_index + 1
    
    while(i < len(array)):
        if min_value > array[i]:
            min_value = array[i]
            min_index = i
        
        i=i+1    
    return min_index
    
def selection_sort(array):
    i = 0
    while(i < len(array)):
        min_index = find_min_index(array, i)
        swap(array, i, min_index)
        i = i+1
    return array
    

array = [22, 11, 99, 88, 9, 7, 42];
print(selection_sort(array) == [7, 9, 11, 22, 42, 88, 99])
