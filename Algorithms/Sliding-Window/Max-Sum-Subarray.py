# Maximum sum of a contiguous subarray with size k
# E.g.  A = [4,2,1,7,8,1,2,8,1,0], k = 3 would yield 16 from [7, 8, 1] (or [1, 7, 8])

def MaxSumSubarray(A, k):
    maxsum = - sys.maxsize
    currentsum = 0
    for i in range(len(A)):
        
        currentsum += A[i]
        if i >= k:
            currentsum -= A[i-k]
        if currentsum > maxsum:
            maxsum = currentsum
    
    return maxsum
