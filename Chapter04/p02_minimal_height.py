""" Minimal Tree: Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree"""
from graph_and_trees import BinaryTreeNode


def create_binary(array, start, end) -> BinaryTreeNode:
    if start > end:
        return None

    mid = (start + end) // 2
    ret_node = BinaryTreeNode(array[mid])
    ret_node.left = create_binary(array, start, mid - 1)
    ret_node.right = create_binary(array, mid + 1, end)
    return ret_node
