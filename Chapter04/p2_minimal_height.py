''' Minimal Tree: Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree'''


class BinaryNode:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

def create_binary(array, start, end) -> BinaryNode:
    if start > end:
        return None

    mid = int((start + end) / 2)
    ret_node = BinaryNode(array[mid])
    ret_node.left = create_binary(array,start,mid-1)
    ret_node.right = create_binary(array,mid+1,end)
    return ret_node
