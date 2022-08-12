''' Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. '''
from linked_list import LinkedList

def k_to_last(link_list, k):

    n_follow = n_k = link_list.head
    cont = 0
    while n_follow:
        if cont < k:
            cont += 1
        else:
            n_k = n_k.next
        n_follow = n_follow.next
    return n_k.value

test_cases = test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)

def test_k_to_last():
    for link_l, k, expect in test_cases:
        l_l = LinkedList(link_l)
        assert k_to_last(l_l, k) == expect

if __name__ == '__main__':
    test_k_to_last()
