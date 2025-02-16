class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_value_count (root: Node, target: int) -> int:
    """
    Function Purpose: 
        Write a function, tree_value_count, that takes in the root of a binary tree and a target value. 
        The function should return the number of times that the target occurs in the tree.

    Parameters:
        root (Node): the root of the binary tree.
        target: int value to find in the tree.

    Returns:
        int: The count of the number of times the target appears in the tree. 

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)

    Time complexity: 
        O(n) where n is the number of nodes in the tree, as we may need to visit each node exactly once
        during the depth-first traversal.

    Space Complexity: O(h) where h is height of the tree
        - Each recursive call adds a frame to the call stack
        - Maximum depth of recursion equals height of tree
        - Best case (balanced tree): O(log n)
        - Worst case (skewed tree): O(n)

    """
    
    ## RECURSIVE APPROACH
    # Base case: empty node returns 0
    # Check current node's value first
    # If not found, recursively search left and right subtrees
    # Return 1 if target is found in either subtree

    # Base case: Root is None
    if root is None: 
        return 0
        
    return (1 if root.val == target else 0) + tree_value_count(root.left, target) + tree_value_count(root.right, target)

def test_a():
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   6     6
    #  / \     \
    # 4   6     12

    return tree_value_count(a,  6) # -> 3

def test_b():
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   6     6
    #  / \     \
    # 4  6     12

    return tree_value_count(a,  12) # -> 2

def test_c ():
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      7
    #    /   \
    #   5     1
    #  / \     \
    # 1   8     7
    #    /       \
    #   1         1

    return tree_value_count(a, 1) # -> 4

def test_d ():
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      7
    #    /   \
    #   5     1
    #  / \     \
    # 1   8     7
    #    /       \
    #   1         1

    return tree_value_count(a, 9) # -> 0

def test_e():
    return tree_value_count(None, 42) # -> 0

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
