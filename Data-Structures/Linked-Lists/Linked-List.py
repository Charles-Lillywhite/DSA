
class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        else:
            current = self.head
            for _ in range(1, index+1):
                current = current.link
            return current.data

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.length += 1
        
        
    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.addAtHead(val)
        else:
            current = self.head

            while current.link is not None:
                current = current.link
            current.link = Node(val)
            self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
            print('switch to addHead')
            self.addAtHead(val)
        elif index == self.length:
            print('switch to addTail')
            self.addAtTail(val)
        else:
            current = self.head
            for _ in range(1, index):
                current = current.link
            current.link = Node(val, current.link)
            self.length += 1
            
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        elif index == 0:
            self.head = self.head.link
            self.length -= 1
        else:
            current = self.head
            for _ in range(1, index):
                current = current.link
            current.link = current.link.link
            self.length -= 1
        
    
    def printList(self):
        if self.head is None:
            print('Empty')
        else:
            current = self.head
            for _ in range(0, self.length):
                print(f'{current.data} ->', end = ' ')
                current = current.link
        print('None')
        print('\n')
