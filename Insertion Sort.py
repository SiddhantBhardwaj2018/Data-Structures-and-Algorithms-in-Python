
def insertionSort(arr): 
    '''
    My implementation of insertion sort.
    This is O(n^2) algorithm.
    '''
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)
    
insertionSort([5,2,4,6,1,3])
