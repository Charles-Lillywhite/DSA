def BS(nums, target):
    start, end = 0, len(nums) - 1
    
    while start <= end:
        
        mid = (start + end)//2
        if nums[mid] == target: 
          return mid
          # return True (if you just want YES/NO)
        
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1
    # return False (if you just want YES/NO)
