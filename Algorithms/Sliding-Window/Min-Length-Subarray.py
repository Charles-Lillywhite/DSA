# for an array A, and target value k, find the minimum length of a (contiguous) subarray with sum at least equal to k.

import sys

def minWindow(A, k):
    windowSum = 0
    minLen = sys.maxsize
    l = 0
    for r in range(len(A)):
        windowSum += A[r]
        while windowSum >= k:
            minLen = min(minLen, r - l + 1)
            windowSum -= A[l]
            l += 1
    
    return minLen
