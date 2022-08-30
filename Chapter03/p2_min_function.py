''' Design a stack with a function min wich returns the minimun element. 
    Push, pop and min should be O(1)'''

from stack_as_ll import Stack

class StackMin(Stack):
    ''' This is a stack with a min function'''
    def __init__(self):
        self.min_stack = Stack()
        super().__init__()

    def push(self, val=None):
        if (self.min_stack.peek() is None) or (val <= self.min_stack.peek()):
            self.min_stack.push(val)
        super().push(val)

    def pop(self):
        value = super().pop()
        if self.min_stack.peek() == value:
            self.min_stack.pop()
        return value

    def min(self):
        return self.min_stack.peek()

test_cases = [
    ([1,2,3,4,5,6,7,8],[1,1,1,1,1,1,1,1]),
    ([5,4,7,1,1,8],[5,4,4,1,1,1]),
]

def test_stack_min():
    for stack_values, min_values in test_cases:
        a_stack = StackMin()
        for val, min_val in zip(stack_values, min_values):
            a_stack.push(val)
            assert a_stack.min() == min_val

        for min_val in reversed(min_values):
            assert a_stack.min() == min_val
            a_stack.pop()

if __name__ == "__main__":
    test_stack_min()