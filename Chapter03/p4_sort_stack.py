''' Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty'''

from stack_as_ll import Stack

def sort_stack(a_stack: Stack):
    tmp_stack = Stack()
    while not a_stack.is_empty():
        tmp = a_stack.pop()
        while not tmp_stack.is_empty() and tmp < tmp_stack.peek():
            a_stack.push(tmp_stack.pop())
        tmp_stack.push(tmp)

    while not tmp_stack.is_empty():
        a_stack.push(tmp_stack.pop())

test_cases = [
    ([8,3,6,1,5,2,7,4],[1,2,3,4,5,6,7,8]),
    ([100,90,3,5,1,90,70,4],[1,3,4,5,70,90,90,100]),
]

def test_sort_stack():
    for case, sol in test_cases:
        a_stack = Stack()
        for x in case:
            a_stack.push(x)
        sort_stack(a_stack)
        res = []
        while not a_stack.is_empty():
            res.append(a_stack.pop())
        
        assert res == sol

if __name__ == "__main__":
    test_sort_stack()

