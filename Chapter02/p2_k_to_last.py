''' Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. '''

def k_to_last(link_list, k):

    n_follow = n_k = link_list.head
    cont = 0
    while n_follow:
        if cont < k:
            cont += 1
        else:
            n_k = n_k.next
        n_follow = n_follow.next
    return n_k
