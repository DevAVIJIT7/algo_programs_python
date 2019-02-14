/**
  First break and array into smaller array,
  then merge two array into single array
  by comparing each element.
**/

def merge(array, l, m, r):
    l1 = []
    l2 = []
    
    k = l
    i = 0
    j = 0
    
    while(k <= m):
        l1.append(array[k])
        #i = i+1
        k = k+1
        
    while(k <= r):
        l2.append(array[k])
        #j = j+1
        k = k+1
        
    i = 0
    j = 0
    k = l
    
    while(i < len(l1) and j < len(l2)):
        if l1[i] < l2[j]:
            array[k] = l1[i];
            i = i+1
            k = k+1
        else:
            array[k] = l2[j];
            j = j+1
            k = k+1
        
    while(i < len(l1)):
        array[k] = l1[i];
        i = i+1
        k = k+1

    while(j < len(l2)):
        array[k] = l2[j];
        j = j+1
        k = k+1


    return array


def mergeSort(array, l, r):
    if l < r:
      m = int((l + r)/2)

      mergeSort(array, l, m)
      mergeSort(array, m+1, r)
      merge(array, l, m, r)
      
    return array
    
    
array = [3, 7, 12, 14, 2, 6, 9, 11]
print(mergeSort(array, 0, len(array)-1))
