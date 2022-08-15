''' Delete a middle node of a list '''
from linked_list import LinkedList, ListNode

def del_middle_node(p_ll, p_node):
    ''' comparing values. doesn't work for the first node'''
    prev = act = p_ll.head
    while act:
        if act.value == p_node.value:
            prev.next = act.next
            break
        prev = act
        act = act.next

test_cases_one = (
    # list, k, expected
    ((10, 20, 30, 40, 50), ListNode(20), [10, 30, 40, 50]),
    ((10, 20, 30, 40, 50), ListNode(30), [10, 20, 40, 50]),
    ((10, 20, 30, 40, 50), ListNode(40), [10, 20, 30, 50]),
)

def test_del_middle():
    for l_l, node, expected in test_cases_one:
        l_l = LinkedList(l_l)
        del_middle_node(l_l, node)
        assert l_l.values() == expected


def del_middle_node_ref(p_node):
    ''' using reference'''
    p_node.value = p_node.next.value
    p_node.next = p_node.next.next

test_cases = (
    # list, k, expected
    ((10, 30, 40, 50), 20, [10, 30, 40, 50]),
    ((10, 20, 40, 50), 30, [10, 20, 40, 50]),
    ((10, 20, 30, 50), 40, [10, 20, 30, 50]),
)

def test_del_middle_ref():
    for (a, *b, c), node, expected in test_cases:
        l_l = LinkedList([a])
        node = l_l.add(node)
        l_l.add_multiple(b)
        l_l.add(c)
        del_middle_node_ref(node)
        assert l_l.values() == expected

if __name__ == "__main__":
    test_del_middle_ref()
