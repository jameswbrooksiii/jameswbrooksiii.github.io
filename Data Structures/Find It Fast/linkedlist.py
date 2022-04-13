import sys

# Had help here from educative.io: https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python

# nodeeeeee
class Node:
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# da list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # puttin stuff in da list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    # printing da list
    def printLL(self):
        current = self.head
        while(current):
            sys.stdout.write(current.data)
            current = current.next

