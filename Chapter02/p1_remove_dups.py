''' p1_remove_dups.py '''

from linked_list import LinkedList

def remove_dups(link_list):

    values = set()
    follow = link_list.head
    prev = None
    while follow:
        if follow.value in values:
            prev.next = follow.next
        else:
            values.add(follow.value)
            prev = follow
        follow = follow.next

    link_list.tail = prev
    return link_list

test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)


def test_remove_dupes():
    for _ in range(100):
        for values, expected in test_cases:
            expected = expected.copy()
            l_l = LinkedList()
            l_l.add_multiple(values)
            deduped = remove_dups(l_l)
            assert deduped.values() == expected

            deduped.add(5)
            expected.append(5)
            a = deduped.values()
            assert deduped.values() == expected


def example():
    ll = LinkedList.generate(100, 0, 9)
    print(ll)
    remove_dups(ll)
    print(ll)



if __name__ == "__main__":
    test_remove_dupes()