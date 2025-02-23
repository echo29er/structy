from typing import Union

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
        O(n) where n is the number of nodes - each node is processed exactly once during the
        breadth-first traversal.

    Space Complexity: 
        O(w) where w is the maximum width of the tree. This comes from:
        - The queue which holds at most one level's worth of nodes
        - The dictionary storing nodes by level
        - The final result list

    """

    ## ITERATIVE APPROACH USING STACK DUE TO DEPTH FIRST TRAVERSAL
    # This implementation uses an iterative depth-first search (DFS) approach with a stack.
    # While we're getting level ordering, DFS still works because we track each node's level
    # explicitly rather than relying on the traversal order.

    # Trees vs Graphs: An Important Distinction
    # Unlike graph traversal, we don't need to track visited nodes here because trees are
    # acyclic by definition - there's exactly one path from root to any node.

    # Key Implementation Goals:
    # 1. Handle empty trees gracefully
    # 2. Track each node's level while traversing
    # 3. Group nodes efficiently by level without storing redundant information

    # Data Structure Choice:
    # We use two main structures:
    # 1. Stack: For DFS traversal, storing (node, level) pairs
    # 2. Dictionary: Maps levels to lists of node values, allowing O(1) grouping
    
    # Empty tree case - return empty list as there are no levels to process
    if root is None: 
        return []

    # Initialize our core data structures:
    # - Stack starts with root node at level 0
    # - level_map will group node values by their levels
    # - results will hold our final level-ordered lists
    level = 0
    stack = [(root,0)]
    level_map = {}
    results = []
    
    # Process nodes using depth-first traversal 
    while stack: 
        # Pop returns the most recently added node (LIFO - Last In, First Out)
        current_node, level = stack.pop()

        # Ensure we have a list initialized for this level
        # This happens the first time we encounter each level
        if level not in level_map: 
            level_map[level] = []

        # Add the current node's value to its level 
        level_map[level].append(current_node.val) # level: [node_value]

        # Add children to stack with their level (parent's level + 1)
        # We add right child first so left child gets processed first (LIFO)
        if current_node.right: 
            stack.append((current_node.right, level+1))
        if current_node.left: 
            stack.append((current_node.left, level+1))

    # Convert our level map into a list of lists
    # Each inner list contains all nodes at that level
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