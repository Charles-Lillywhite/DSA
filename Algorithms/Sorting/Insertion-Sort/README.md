INSERTION SORT:

- In Bubble Sort, we effectively sorted from end-to-start by pairwise comparison.
- In insertin sort we sort from start-to-end: we consider each element in the list in turn, each time determining where it should exist amongst the previous (sorted) elements.



**Example**
```
arr = [11, 12, 13, 5, 6] 

imagine we've sorted 11, 12, 13 (i = 0,1,2) and now i = 3 index is considered

i = 3 

item = arr[i] # the value we want to compare to

j = i - 1 # start j one left of i

while j >= 0 and arr[j] > item: # consider all entries to left of item which are less than item
    
    arr[j+1] = arr[j] # move each element up 1 place
    j -= 1
    
arr[j+1] = item # ie put item where it belongs. ([j + 1], not[j],  as the last j -= 1 moves into the already-sorted elements)
```
