# Implementation with Python LIST

class ListQueueSimple:
    
    def __init__(self):
        self.L = []
        
    def enqueue(self, item):
        self.L.append(item)
    
    def dequeue(self):
        return self.L.pop(0)
    
    def peek(self):
        return self.L[0]
    
    def __len__(self):
        return len(self.L)
    
    def isempty(self):
        return len(self) == 0
