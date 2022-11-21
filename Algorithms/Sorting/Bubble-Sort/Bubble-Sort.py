def bubbleSort(arr):
    for iteration in range(0, len(arr) - 1):
        for j in range(0, len(arr) - iteration - 1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
