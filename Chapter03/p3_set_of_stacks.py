''' Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.'''

from stack_as_ll import Stack

class SetOfStacks:
    def __init__(self, limit=10) -> None:
        self.capacity = limit
        self.stacks = [Stack()]
        self.stack_ix = 0
        self.stacks_sizes = [0]

    def push(self, item):
        if self.stacks_sizes[self.stack_ix] < self.capacity:
            self.stacks[self.stack_ix].push(item)
            self.stacks_sizes[self.stack_ix] +=1
        else:
            self.stack_ix +=1
            self.stacks.append(Stack())
            self.stacks[self.stack_ix].push(item)
            self.stacks_sizes.append(1)

    def pop(self):
        item = self.stacks[self.stack_ix].pop()
        self.stacks_sizes[self.stack_ix] -=1
        if self.stacks_sizes[self.stack_ix] == 0 and self.stack_ix != 0:
            del self.stacks_sizes[self.stack_ix]
            del self.stacks[self.stack_ix]
            self.stack_ix -= 1
        return item

