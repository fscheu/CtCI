'''Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> 0 -> E -> C
Output: C
'''
import time
import random
from typing import Optional
from linked_list import LinkedList, ListNode

def find_loop(ll: LinkedList) -> Optional[ListNode]:
    seg = ll.head
    visited = set()
    while seg:
        if seg in visited:
            return seg
        visited.add(seg)
        seg = seg.next
    return None

def find_loop_fl(ll: LinkedList) -> Optional[ListNode]:
    fast = slow = ll.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            break

    if not fast or not fast.next:
        return None

    slow = ll.head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow

def test_find_loop():
    start = time.perf_counter()
    for _ in range(1000):
        l_circle = LinkedList.generate(random.randint(1,1000),0,100)
        l_loop = LinkedList.generate(random.randint(1,1000),0,100)
        l_circle.tail.next = l_circle.head
        l_loop.tail.next = l_circle.head
        assert find_loop_fl(l_loop) == l_circle.head
    duration = time.perf_counter() -start
    print(f"duration: {duration :.1f}ms")

if __name__ == "__main__":
    test_find_loop()
    