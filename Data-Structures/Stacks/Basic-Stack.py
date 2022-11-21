# Implementation with Python LIST

class ListStack:
    
    def __init__(self):
        self.L = []
    
        
    def push(self, item):
        self.L.append(item)
        
    def pop(self):
        return self.L.pop()
    
    def peek(self):
        return self.L[-1]
    
    def __len__(self):
        return len(self.L)
    
    def isempty(self):
        return len(self) == 0
