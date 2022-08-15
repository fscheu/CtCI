''' Partition a list around a given value'''
from linked_list import LinkedList

def partition_list(p_ll: LinkedList, p_value) -> LinkedList:
    ll_part1 = LinkedList()
    ll_part2 = LinkedList()
    node = p_ll.head
    while node:
        if node.value >= p_value:
            ll_part2.add(node.value)
        else:
            ll_part1.add(node.value)
        node = node.next
    ll_part1.add_multiple(ll_part2.values())
    return ll_part1

def example():

    ll = LinkedList.generate(10, 0, 99)
    print(ll)
    ll = partition_list(ll, ll.head.value)
    print(ll)


if __name__ == "__main__":
    example()
