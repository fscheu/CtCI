''' Linked List structure definition '''
import random

class ListNode():
    def __init__(self, val, n_node=None, p_node=None):
        self.value = val
        self.next = n_node
        self.prev = p_node

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self, val=None):
        self.head = None
        self.tail = None
        if val is not None:
            self.add_multiple(val)

    def add(self, val):
        ''' Adds a value to the end of the LinkedList'''
        if self.head is None:
            self.head = self.tail = ListNode(val)
        else:
            self.tail.next = ListNode(val, p_node=self.tail)
            self.tail = self.tail.next
        return self.tail

    def add_multiple(self, a_list):
        for x in a_list:
            self.add(x)

    def __str__(self) -> str:
        return ' -> '.join([str(x) for x in self])

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def values(self):
        ''' Returns a standard list with all the values of the LinkedList'''
        return [x.value for x in self]

    @classmethod
    def generate(cls, k, min_value, max_value):
        '''Generate a LinkedList with random values'''
        return cls(random.choices(range(min_value, max_value), k=k))
