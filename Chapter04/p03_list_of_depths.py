'''List of Depths: Given a binary tree, design an algorithm which creates a linked list of all
the nodes at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).'''

from graph_and_trees import BinaryTreeNode
from p02_minimal_height import create_binary

def list_depths(a_list, node:BinaryTreeNode, level=0):

    if len(a_list) <= level:
        a_list.append([])
    a_list[level].append(node.value)
    if node.left:
        list_depths(a_list,node.left,level+1)
    if node.right:
        list_depths(a_list,node.right,level+1)

test_cases = [
    ([3,4,1,0,2,5,6],[[0], [4, 5], [3, 1, 2, 6]]),
    ([7,3,8,4,9,1,10,0,2,5,6],[[1], [8, 2], [7, 4, 10, 5], [3, 9, 0, 6]]),
]

def test_list_depths():

    for tree, result in test_cases:
        root = create_binary(tree,0,len(tree)-1)
        levels = []
        list_depths(levels,root)
        print(f"root: {root}")
        print(f"levels: {levels}")
        assert levels == result


if __name__ == "__main__":
    test_list_depths()
