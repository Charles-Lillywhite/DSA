INSERTION SORT:

- In Bubble Sort, we effectively sorted from end-to-start by pairwise comparison.
- In insertion sort we effectively sort from start-to-end.
- We consider each element in the list in turn - each time determining where it should exist amongst the previous (sorted) elements - before **inserting** it at the correct loation.
- Worst case is &Omicron;(n^2) when array is sorted in reverse order, and best case is &Omega;(n) when already correctly sorted.


**Example**
```
arr = [11, 12, 13, 5, 6] 

imagine we've sorted 11, 12, 13 (i = 0,1,2) and now i = 3 index is considered

i = 3 

item = arr[i] # the value we want to compare to

j = i - 1 # start j one left of i

while j >= 0 and arr[j] > item: # consider all entries to left of item which are greater than item
    
    arr[j+1] = arr[j] # move each element up 1 place
    j -= 1
    
arr[j+1] = item # ie put item where it belongs. ([j + 1], not[j],  as the last j -= 1 moves us one index left of the correct place to insert)
```
