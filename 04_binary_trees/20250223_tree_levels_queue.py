from typing import Union
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_levels (root: Node) -> list[list[Union[int, str]]]:
    """
    Function Purpose: 
        Write a function, tree_levels, that takes in the root of a binary tree. 
        The function should return a 2-Dimensional list where each sublist represents a level of the tree.

    Parameters:
        root (Node): the root of the binary tree.

    Returns:
        list[list[Union[int, str]]]: a 2d array where each inner array is a level of the tree and the outer array is the collection of the levels.
    
    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - You may assume that the input tree is non-empty

    Time complexity: 
        O(n) where n is the number of nodes in the tree:
        - Each node is visited exactly once
        - Level grouping operations are O(1) using dictionary

    Space Complexity: 
        O(w) where w is the maximum width of the tree:
        - Queue stores at most one level's worth of nodes
        - Dictionary stores node values grouped by level
        - Both are bounded by the tree's maximum width
        - Final result takes O(n) space to store all node values

    """

    ## ITERATIVE APPROACH USING STACK DUE TO DEPTH FIRST TRAVERSAL
    # This implementation uses breadth-first search (BFS) to traverse the tree level by level.
    # BFS is particularly well-suited for level-order traversal as it naturally processes 
    # all nodes at the current level before moving to the next level.

    # Trees vs Graphs: A Key Distinction
    # In trees, we don't need to track visited nodes because trees are acyclic by definition.
    # There's exactly one path from the root to any node, so we'll never revisit a node.

    # Implementation Strategy:
    # We use two main data structures to efficiently capture level information:
    # 1. Queue: Processes nodes in FIFO (First In, First Out) order, maintaining level order
    # 2. Dictionary: Groups nodes by their level for easy retrieval and organization

    # Time and Space Efficiency:
    # By using a dictionary to group nodes by level as we traverse, we avoid:
    # - Creating separate lists for each level during traversal
    # - Multiple passes through the tree
    # - Excessive memory usage from duplicating node information
    
    # Empty tree
    if root is None: 
        return []

    # Initialize our data structures:
    # - Queue starts with root node at level 0, using deque for O(1) operations
    # - level_map will group node values by their level
    # - results will store our final ordered list of levels
    level = 0
    queue = deque([(root,0)]) # Using deque for efficient queue operations # Each entry is (node, level) pair
    level_map = {}
    results = []
    
    # Process nodes level by level
    while queue: 
        # popleft() gives us FIFO behavior - essential for processing levels in order
        current_node, level = queue.popleft()

        # Create new level list in dictionary if this is first node at this level
        if level not in level_map: 
            level_map[level] = []

        # Add the current node's value to its level 
        level_map[level].append(current_node.val) # level: [node_value]

        # Add children to the queue left to right to maintain FiFo
        if current_node.left: 
            queue.append((current_node.left, level+1))
        if current_node.right: 
            queue.append((current_node.right, level+1))

    # Convert level map to list of lists, maintaining level order
    for key in level_map: 
        results.append(level_map[key])

    return results

def test_a():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    return tree_levels(a) # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f']
    # ]

def test_b():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #         a
    #      /    \
    #     b      c
    #   /  \      \
    #  d    e      f
    #      / \    /
    #     g  h   i

    return tree_levels(a) # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f'],
    #   ['g', 'h', 'i']
    # ]

def test_c():
    q = Node('q')
    r = Node('r')
    s = Node('s')
    t = Node('t')
    u = Node('u')
    v = Node('v')

    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v

    #      q
    #    /   \
    #   r     s
    #    \
    #     t
    #    /
    #   u
    #  /
    # v

    return tree_levels(q) # ->
    # [
    #   ['q'],
    #   ['r', 's'],
    #   ['t'],
    #   ['u'],
    #   ['v']
    # ]

def test_d():
    return tree_levels(None) # -> []


print(test_a())
print(test_b())
print(test_c())
print(test_d())