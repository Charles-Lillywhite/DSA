class ListQueueFakeDelete:
  
    # dequeue method is changed
    
    def dequeue(self):
        item = self.peek()
        self.head += 1
        if self.head > len(self.L) // 2:
            self.L = self.L[self.head: ]
            self.head = 0
        return item
    
    
    # all other methods same as 'fake-delete' queue
    
    def __init__(self):
        self.head = 0
        self.L = []
        
    def enqueue(self, item):
        self.L.append(item)
        
    def peek(self):
        return self.L[self.head]
    
    def __len__(self):
        return len(self.L) - self.head
    
    def isempty(self):
        return len(self) == 0
