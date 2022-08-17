''' Implement a function to check if a LinkedList is a palindrome'''
import time
from linked_list import LinkedList, ListNode

def palindrome_double_ll(p_ll: LinkedList) -> bool:
    ''' check if a double linked list is a palindrome'''
    seg_h = p_ll.head
    seg_t = p_ll.tail
    while seg_h != seg_t:
        if seg_h.value != seg_t.value:
            return False
        seg_h = seg_h.next
        seg_t = seg_t.prev
    return True

def reverse_list(node: ListNode, prev=None) -> ListNode:
    ''' returns the reverse of a list creating a copy - recursive'''
    if not node:
        return prev
    new_node = ListNode(node.value, n_node=prev)
    return reverse_list(node.next, prev=new_node)

def compare_lists(node_one, node_two) -> bool:
    while node_one and node_two:
        if node_one.value  != node_two.value:
            return False
        node_one = node_one.next
        node_two = node_two.next
    return True

def palindrome_iterative(p_ll: LinkedList) -> bool:
    '''check if a linked list is a palindrome using two pointers'''
    seg_f = seg_s = p_ll.head

    #Take the slow pointer to the middle
    advance_slow = False
    while seg_f:
        if advance_slow:
            seg_s = seg_s.next
        seg_f = seg_f.next
        advance_slow = not advance_slow

    #Reverse the half of the list
    half_list = reverse_list(seg_s)
    seg_f = p_ll.head
    #Return comparison
    return compare_lists(seg_f, half_list)

test_cases = [
    ([1, 2, 3, 4, 3, 2, 1], True),
    ([1], True),
    (["a", "a"], True),
    ("aba", True),
    ([], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2], False),
]

testable_functions = [
    palindrome_iterative,
    palindrome_double_ll,
]

def test_is_palindrome():
    for f in testable_functions:
        start = time.perf_counter()
        for values, expected in test_cases:
            print(f"{f.__name__}: {values}")
            for _ in range(100):
                assert f(LinkedList(values)) == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    test_is_palindrome()
