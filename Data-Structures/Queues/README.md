The Queue ADT will have the following functionalities:

- enqueue(item) (add an item to the end of the queue)

- dequeue (remove item at the front of the queue, FIFO)

- peek (return, without removing, the next item in the queue, FIFO order)

- len() (the number of items in the queue, will need dunder for abstract object)

- isempty (returns True of length is zero, False otherwise)

The obvious inefficiency here is the dequeue operation, as popping the 0th element in a list is an O(N) operation!
Even if we dequeued from the end of the list, we'd have to append from the front, which is likewise O(N).
We can get around this with a bit of a fudge; let's not actually delete any elements, but keep a track of the head (front) of our queue.
__This is the implementation in 'Queue-Fake-Delete.py'__


However it still feels somewhat inefficient to have lots of 'dead weight' (ie items in the list which do not feature in the queue). 
Let's compromise by only deleting the redundant elements once they comprise more than half of the length of the list which is powering our queue.
__This is the implementation in 'Queue-Partial-Delete.py'__

__Although we have lost some of the advantage of our fake delete, the average cost per item dequeued is constant! 
A good explanation of this is provided in Don Sheehy's Python DSA notes, available online__

