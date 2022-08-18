'''
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
'''
import time
import random
from linked_list import LinkedList, ListNode

def are_intersections_bf(ll_1, ll_2) -> ListNode:
    seg_1 = ll_1.head
    while seg_1:
        seg_2 = ll_2.head
        while seg_2:
            if seg_1 is seg_2:
                return seg_1
            seg_2 = seg_2.next
        seg_1 = seg_1.next
    return None

def len_and_tail(ll: LinkedList):
    seg = ll.head
    if not seg:
        return 0, seg

    count = 1
    while seg.next:
        count += 1
        seg = seg.next
    return count, seg

def are_intersections(ll_1, ll_2) -> ListNode:

    len_1, tail_1 = len_and_tail(ll_1)
    len_2, tail_2 = len_and_tail(ll_2)

    if tail_1 is not tail_2:
        return None

    long = ll_1.head if len_1 >= len_2 else ll_2.head
    short = ll_1.head if len_1 < len_2 else ll_2.head
    dif_len = abs(len_1 - len_2)
    for _ in range(dif_len):
        long = long.next

    while long is not short:
        long = long.next
        short = short.next
    return long

def test_intersections():

    start = time.perf_counter()
    for _ in range(1000):
        l_tail = LinkedList.generate(random.randint(1,30), 0, 99)
        l_list1 = LinkedList.generate(random.randint(1,30), 0, 99)
        l_list2 = LinkedList.generate(random.randint(1,30), 0, 99)
        l_list1.tail.next = l_tail.head
        l_list2.tail.next = l_tail.head
        #print(l_list1)
        #print(l_list2)
        assert are_intersections(l_list1, l_list2) == l_tail.head
    duration = time.perf_counter() - start
    print (f"duration: {duration * 1000:.1f}ms")




if __name__ == "__main__":
    test_intersections()
