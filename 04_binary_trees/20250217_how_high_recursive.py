class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def how_high (root: Node) -> int:
    """
    Function Purpose: 
        Write a function, how_high, that takes in the root of a binary tree. 
        The function should return a number representing the height of the tree.

        The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

        If the tree is empty, return -1.

    Parameters:
        root (Node): the root of the binary tree.

    Returns:
        int: The height of the tree i.e. the maximal number of edges from the root node to any leaf node. 
        
    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)

    Time complexity: 
        O(n) where n is the number of nodes in the tree, as we have to visit each node in the tree. 

    Space Complexity: O(h) where h is height of the tree
        - O(h) for a skewed tree
        - O(log(n)) for a balance tree

    """

    ## RECURSIVE APPROACH 

    # Base case: Root is None
    if root is None: 
        return -1
    
    # Base case 2: if we're at a leaf node, return 0
    if root.left is None and root.right is None:
        return 0
    
    # We want to traverse a branch and add 1 every time. 
    left_path = (how_high(root.left) + 1)
    right_path = (how_high(root.right) + 1)
    
    return max(left_path, right_path)

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

    return how_high(a) # -> 2

def test_b():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    return how_high(a) # -> 3

def test_c ():
    a = Node('a')
    c = Node('c')

    a.right = c

    #      a
    #       \
    #        c

    return how_high(a) # -> 1

def test_d ():
    a = Node('a')

    #      a

    return how_high(a) # -> 0

def test_e():
    return how_high(None) # -> -1


print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())