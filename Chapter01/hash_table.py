#   HashTable implementation
#   with an array of LinkedList
#
#

class LinkedList:
    def __init__(self, val=None, a_next=None) -> None:
        self.val=val
        self.next = a_next

    def add(self, val):
        new_node = LinkedList(val, self)
        self = new_node

class HashTable:
    def __init__(self,size):
        self.values = size * [None]

    def __len__(self):
        return len(self.values)

    def hash_func(self, val):
    # It uses repr to obtain a string representation of the object
    # It removes the "'" to better distribute the results of ord
    # It uses enumerate and index to improve distribution in similar str
    # Enumerate starts at 1 so don't multiply by zero the first value
        return sum(
            index * ord(character)
            for index, character in enumerate(repr(val).lstrip("'"), 1)
        )


    def add(self, val=None):

        if val is None:
            return

        hash_code = self.hash_func(val)
        position = hash_code % len(self.values)
        if self.values[position] is None:
            self.values[position] = LinkedList(val)
        else: 
            self.values[position].add(val)

    def get(self, val=None):

        if val is None: return

        hash_code = self.hash_func(val)
        position = hash_code % len(self.values)
        seg =  self.values[position]
        while seg:
            if seg.val == val:
                return seg.val
            else:
                seg = seg.next
        return None

