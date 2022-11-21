# Do not actually pop (as this is O(N)), instead use two pointer and update queue head.

class ListQueueFakeDelete:
    
    def __init__(self):
        self.head = 0
        self.L = []
        
    def enqueue(self, item):
        self.L.append(item)
        
    def peek(self):
        return self.L[self.head]
    
    def dequeue(self):
        item = self.peek()
        self.head += 1
        return item
    
    def __len__(self):
        return len(self.L) - self.head
    
    def isempty(self):
        return len(self) == 0
