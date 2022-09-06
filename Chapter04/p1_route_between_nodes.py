from collections import deque
from graph_and_trees import Node

def dfs_route(node1: Node, node2: Node, visited: None):

    visited = set() if visited is None else visited
    for x in node1.neighbors:
        if x not in visited:
            visited.append(x)
            if x is node2 or dfs_route(x, node2,visited):
                return True
    return False

def bfs_route(node1: Node, node2: Node):
    to_visit = deque()
    to_visit.append(*node1.neighbors)
    visited = set()
    visited.add(node1)
    for x in to_visit:
        if x not in visited:
            if x is node2:
                return True
            visited.add(x)
            to_visit.append(*x.neighbors)
    return False
