/** 
  Directions
    Given an array and chunk size, divide the array into many subarrays
    where each subarray is of length size
      Examples
        chunk([1, 2, 3, 4], 2) => [[ 1, 2], [3, 4]]
        chunk([1, 2, 3, 4, 5], 2) => [[ 1, 2], [3, 4], [5]]
        chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) => [[ 1, 2, 3], [4, 5, 6], [7, 8]]
        chunk([1, 2, 3, 4, 5], 4) => [[ 1, 2, 3, 4], [5]]
        chunk([1, 2, 3, 4, 5], 10) => [[ 1, 2, 3, 4, 5]]
**/

def chunk(array, s):
    r = len(array)
    j = 0
    res = []
    while(j < r):
        res.append(array[j:j+s])
        j = j + s
    
    return res
    
print(chunk([1,2,3,4,5], 2))
print(chunk([1, 2, 3, 4, 5, 6, 7, 8], 3))
