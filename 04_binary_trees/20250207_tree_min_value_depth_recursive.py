class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_min_value (root: Node) -> int:
    """
    Function Purpose: 
        Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. 
        The function should return the minimum value within the tree.

    Args:
        root (Node): the root of the binary tree.

    Returns:
        int: The minimum value in the tree.

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - Node values are all positive or negative integers. 
        - You may assume that the input tree is non-empty.

    Time complexity: 
        O(n) where n is number of nodes because:
        - We have to visit each node once

    Space complexity: 
        O(h) where h is the height of the tree because:
        - The recursive call stack will go as deep as the height of the tree
        - In the worst case (completely unbalanced tree), h = n
        - In the best case (perfectly balanced tree), h = log(n)
    """

    ## RECURSIVE APPROACH
    # Base case: there's only a root. 
    # Check current node's value first

    # We'll use the guess and check pattern. Where we'll assume the first value is the smallest and compare it with each subsequent.
    smallest_value = root.val

    # Base case: only a root.
    if root.left is None and root.right is None: 
        return smallest_value

    # Recursive case: check left subtree 
    if root.left is not None:
        left_min = tree_min_value(root.left)
        smallest_value = min(smallest_value, left_min)

    # Recursive case: check right subtree 
    if root.right is not None:
        right_min = tree_min_value(root.right)
        smallest_value = min(smallest_value, right_min)     
    
    return smallest_value

def test_a():
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1
    return tree_min_value(a) # -> -2

def test_b():
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(14)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       5
    #    /    \
    #   11     3
    #  / \      \
    # 4   14     12

    return tree_min_value(a) # -> 3

def test_c ():
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(-2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     /       \
    #    -2       -2

    return tree_min_value(a) # -> -13

def test_d ():
    a = Node(42)

    #        42

    return tree_min_value(a) # -> 42


print(test_a())
print(test_b())
print(test_c())
print(test_d())