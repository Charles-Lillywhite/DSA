def bubbleSort(arr):
    
    for iteration in range(0, len(arr) - 1):
        
        isSorted = True
        
        for j in range(0, len(arr) - iteration - 1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = False
        
        if isSorted:
            return arr
      

    return arr
