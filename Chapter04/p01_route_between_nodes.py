'''Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes. '''

from collections import deque
import time
from graph_and_trees import Node

def dfs_route(node1: Node, node2: Node, visited: None):

    visited = set() if visited is None else visited
    for x in node1.neighbors:
        if x not in visited:
            visited.add(x)
            if x is node2 or dfs_route(x, node2,visited):
                return True
    return False

def bfs_route(node1: Node, node2: Node):
    to_visit = deque()
    to_visit.append(node1)
    visited = set()
    while to_visit:
        node = to_visit.popleft()
        for x in node.neighbors:
            if x not in visited:
                if x is node2:
                    return True
                to_visit.append(x)
        visited.add(node)
    return False

def bidirectional_route(start: Node, end: Node):
    to_visit = deque()
    to_visit.append(start)
    to_visit.append(end)
    visited_start = set()
    visited_start.add(start)
    visited_end = set()
    visited_end.add(end)
    while to_visit:
        node = to_visit.popleft()

        if node in visited_start and node in visited_end:
            return True

        for y in node.neighbors:
            if node in visited_start and y not in visited_start:
                visited_start.add(y)
                to_visit.append(y)
            if node in visited_end and y not in visited_end:
                visited_end.add(y)
                to_visit.append(y)
            

    return False

nA = Node('A')
nB = Node('B')
nC = Node('C')
nD = Node('D')
nE = Node('E')
nF = Node('F')
nG = Node('G')
nH = Node('H')
nI = Node('I')
nO = Node('O')
nJ = Node('J')
nK = Node('K')
nL = Node('L')
nP = Node('P')
nQ = Node('Q')
nR = Node('R')
nA.neighbors = [nB, nC]
nB.neighbors = [nD]
nC.neighbors = [nD,nE]
nD.neighbors = [nB, nC]
nE.neighbors = [nC, nF]
nF.neighbors = [nE, nO, nI, nG]
nG.neighbors = [nF, nH]
nH.neighbors = [nG]
nI.neighbors = [nF, nJ]
nO.neighbors = [nF]
nJ.neighbors = [nK, nL, nI]
nK.neighbors = [nJ]
nL.neighbors = [nJ]
nP.neighbors = [nQ, nR]
nQ.neighbors = [nP, nR]
nR.neighbors = [nP, nQ]

tests_cases = [
    (nA, nL, True),
    (nA, nB, True),
    (nH, nK, True),
    (nL, nD, True),
    (nP, nQ, True),
    (nQ, nP, True),
    (nQ, nG, False),
    (nR, nA, False),
    (nP, nB, False),
]

def test_routes():

    ts = time.perf_counter()
    for _ in range(1000):
        for start, end, result in tests_cases:
            assert dfs_route(start,end,None) == result
    te = time.perf_counter()
    print(f'dfs_route took {te-ts:0.4f}')

    ts = time.perf_counter()
    for _ in range(1000):
        for start, end, result in tests_cases:
            assert bfs_route(start,end) == result
    te = time.perf_counter()
    print(f'bfs_route took {te-ts:0.4f}')

    ts = time.perf_counter()
    for _ in range(1000):
        for start, end, result in tests_cases:
            assert bidirectional_route(start,end) == result
    te = time.perf_counter()
    print(f'bidirectional_route took {te-ts:0.4f}')

if __name__ == '__main__':
    test_routes()