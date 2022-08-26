''' Implementing a Stack as a Linked List'''

class StackNode:
    def __init__(self, d=None, n=None):
        self.data = d
        self.next = n

class Stack:

    def __init__(self):
        self.head = None

    def push(self, val=None):
        ''' Adds a value to the top of the Stack'''
        new_node = StackNode(val, self.head)
        self.head = new_node

    def pop(self):
        '''Remove and return the value at the top of the Stack'''
        value = self.head.data
        self.head = self.head.next
        return value

    def peek(self):
        '''Returns the value from the top of the Stack'''
        return self.head.data

    def is_empty(self):
        return bool(self.head)
