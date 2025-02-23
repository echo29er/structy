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
        - Each node is visited exactly once through recursion
        - The while loop that extends the levels list runs at most h times total
          (where h is the height of the tree), not per node
        - Appending to a list is an O(1) operation

    Space Complexity: 
        O(n) where n is the number of nodes in the tree. This comes from:
        - O(h) recursive call stack space, where h is the height of the tree
          - In a balanced tree, h is O(log n)
          - In worst case (skewed tree), h becomes O(n)
        - O(n) space for the final levels list storing all node values
        - Unlike the iterative solution, we don't get the O(w) space benefit
          because the recursive call stack can grow to O(n) in worst case

    """
    

    # This helper function will do the recursive traversal
    def traverse(node: Node, level: int, levels: list[list]) -> None:
        # Base case: if node is None, we can't add anything
        if not node:
            return
            
        # If this is the first node we've seen at this level,
        # we need to create a new sublist for this level
        while len(levels) <= level:
            levels.append([])
            
        # Add the current node's value to its level's sublist
        levels[level].append(node.val)
        
        # Recursively process children at the next level
        traverse(node.left, level + 1, levels)
        traverse(node.right, level + 1, levels)
    
    # Handle empty tree case
    if not root:
        return []
        
    # Initialize our result list and start the recursion
    levels = []
    traverse(root, 0, levels)
    return levels

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