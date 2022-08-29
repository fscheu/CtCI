''' Three in One: Describe how you could use a single array to implement three stacks '''
import pytest

class FixedStacks:
    def __init__(self, size=10, amount=1) -> None:
        '''Creates the amount of Stacks of the size indicated'''
        self.array = [0] * (size * amount)
        self.nro_stacks = amount
        self.size_stacks = size
        self.ix_stack = [0] * amount

    def push(self, stack, value):
        if 0 <= stack <= (self.nro_stacks-1):
            if self.ix_stack[stack] < self.size_stacks:
                location = stack * self.size_stacks + self.ix_stack[stack]
                self.array[location] = value
                self.ix_stack[stack] += 1
                return None
            raise StackFullException
        raise InvalidStackException

    def pop(self, stack):
        if 0 <= stack <= (self.nro_stacks-1):
            if self.ix_stack[stack] > 0:
                location = stack * self.size_stacks + self.ix_stack[stack] - 1
                value = self.array[location]
                self.array[location] = 0
                self.ix_stack[stack] -= 1
                return value
            raise StackEmptyException
        raise InvalidStackException

    def peek(self, stack):
        if 0 <= stack <= (self.nro_stacks-1):
            if self.ix_stack[stack] > 0:
                location = stack * self.size_stacks + self.ix_stack[stack] - 1
                return self.array[location]
            raise StackEmptyException
        raise InvalidStackException

class StackFullException(Exception):
    "Stack is Full"

class InvalidStackException(Exception):
    "Invalid Stack referenced"

class StackEmptyException(Exception):
    "The stack is empty"

def test_fixed_stacks():
    size = 16
    nro_stacks = 4
    stack = FixedStacks(size, nro_stacks)

    for i in range(nro_stacks):

        with pytest.raises(StackEmptyException):
            stack.pop(i)

        for v in range(size):
            stack.push(i,v)
            assert stack.peek(i) == v

        with pytest.raises(StackFullException):
            stack.push(i,v)

if __name__ == "__main__":
    test_fixed_stacks()
        