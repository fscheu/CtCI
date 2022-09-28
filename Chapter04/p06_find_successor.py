"""Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent."""

from graph_and_trees import BinaryNode


def left_mose_child(node):
    """ Return the left most child of a given node"""
    next_node = node
    while next_node.left:
        next_node = next_node.left
    return next_node


def find_successor(node: BinaryNode):
    """return the next node in-order traversal"""
    if node.right:
        # if it has a right child, return the left most node
        return left_mose_child(node.right)

    if node.parent:

        if node == node.parent.left:
            # if this node was a left child the next node is the parent
            return node.parent
        else:
            # if this node was the right child the next node is the next
            # right-left most sibling
            next_node = node.parent
            while next_node.parent and next_node == next_node.parent.right:
                next_node = next_node.parent
            return next_node.parent
