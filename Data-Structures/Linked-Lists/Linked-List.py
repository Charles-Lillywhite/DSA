'''
In a standard array, item are stored sequentially in a contiguous block of memory.
In a linked list this is not the case; each 'node' contains the value of
the data item, as well as a pointer to the memory location of the next element.

Linked lists are a simple data structure for storing a sequential collection.
Unlike a standard Python list, it will allow us to insert at the beginning
quickly. The idea is to store the items in individual objects called nodes.
A special node is the head of the list (we may also denote the tail of the list, and include pointers in both directions).
Each node stores a reference to the next node in the list.
'''
        
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
