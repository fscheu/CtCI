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
        self.size = 0

    def push(self, item):
        cur_stack = self.get_cur_stack()
        if self.size < self.capacity:
            cur_stack.push(item)
            self.size +=1
        else:
            self.stacks.append(Stack())
            self.stacks[-1].push(item)
            self.size = 1

    def pop(self):
        cur_stack = self.get_cur_stack()
        item = cur_stack.pop()
        self.size -=1
        if self.size == 0 and len(self.stacks) > 1:
            del self.stacks[-1]
            self.size = self.capacity
        return item

    def get_cur_stack(self):
        return self.stacks[-1]

def test_stacks():
    stacks = SetOfStacks(5)
    for i in range(35):
        stacks.push(i)
    lst = []
    for _ in range(35):
        lst.append(stacks.pop())
    assert lst == list(reversed(range(35)))

if __name__ == "__main__":
    test_stacks()
