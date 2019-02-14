/**
  Get the pivot element and partition based on
  that pivot element.Put all less than elements
  from the pivot element to the left side and
  greater than elements to the right side.
**/

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    
def partition(array, l, r):
    i = l
    
    while(i < r):
        if(array[i] <= array[r]):
            swap(array, i, l)
            l = l+1
            
        i = i+1
    swap(array, i, l)
    return l

def quick_sort(array, l, r):

    if l < r:
        p = partition(array, l, r)

        quick_sort(array, l, p-1)
        quick_sort(array, p+1, r)
        
    return array
        

array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 4, 6]        
print(quick_sort(array, 0, len(array) -1))
