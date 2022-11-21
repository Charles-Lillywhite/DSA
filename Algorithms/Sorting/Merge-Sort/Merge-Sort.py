def mergeSort(arr):
    
    if len(arr)>1: # need this statement to avoid endless recursion. A single(/zero)-element arr is already sorted
         
        mid = len(arr)//2

        L = arr[:mid] # break the array into two smaller halves
        R = arr[mid:]

        #recursion, this recurses all the way down to atomic arrays

        mergeSort(L) # merge-sort each half
        mergeSort(R)

        # Add atomic elements back together, this recurses all the way back up

        i = j = k = 0

        while i < len(L) and j < len(R): # add elements back together piecewise from L,R depending on size
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L): # any left over elements if L bigger than R
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R): # OR any left over elements if R bigger than L
            arr[k] = R[j]
            j += 1
            k += 1

    
    return arr
        
