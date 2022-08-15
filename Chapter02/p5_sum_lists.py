''' Sum two numbers represented by numbers in a linked list'''
from linked_list import LinkedList

def val_or_zero(p_node) -> int:
    return 0 if p_node is None else p_node.value

def next_or_none(p_node):
    return None if p_node is None else p_node.next


def sum_linked_list(p_one: LinkedList, p_two: LinkedList) -> LinkedList:
    ''' sum the numbers in two linked list and return a list with the result'''
    ll_result = LinkedList()
    seg_one = p_one.head
    seg_two = p_two.head
    rest = value = 0
    while seg_one or seg_two:
        value = val_or_zero(seg_one) + val_or_zero(seg_two) + rest
        if value >= 10:
            rest = value // 10
            value = value % 10
        else:
            rest = 0
        ll_result.add(value)
        seg_one = next_or_none(seg_one)
        seg_two = next_or_none(seg_two)
    if rest:
        ll_result.add(rest)
    return ll_result

test_cases = (
    # all values can either be list of integer or integers
    # a, b, expected_sum
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    ([0], [0], [0]),
    ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
    ([1,2,3], [1,2,3], [2,4,6]),
    ([1,2,3], [1], [2,2,3]),
    ([1], [1,2,3], [2,2,3]),
)

def test_sum_ll():
    for a, b, exp in test_cases:
        ll_a = LinkedList(a)
        ll_b = LinkedList(b)
        res = sum_linked_list(ll_a, ll_b)
        assert res.values() == exp

if __name__ == "__main__":
    test_sum_ll()