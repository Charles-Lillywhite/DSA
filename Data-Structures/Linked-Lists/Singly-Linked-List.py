class Node:
    def __init__(self, value, link = None):
        self.val = value
        self.link = link

class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        
    def get(self, index: int) -> int:
        
        if index < 0 or index > self.length - 1:
            return -1
        
        current = self.head
        for _ in range(1, index + 1):
            current = current.link
        return current.val
    
    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
        else:
            current = self.head
            while current.link:
                current = current.link
            current.link = Node(val)

            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            current = self.head
            for _ in range(1, index):
                current = current.link
            current.link = Node(val, current.link)
            self.length += 1
            
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length - 1:
            return
        elif index == 0:
            self.head = self.head.link
            
        else:
            current = self.head
            for _ in range(1, index):
                current = current.link
            current.link = current.link.link
        
        self.length -= 1
        
        
    def printList(self):
        for idx in range(self.length):
            currentVal = self.get(idx)
            print(currentVal, end = ' - ')
        print('None')
        print('\n')
