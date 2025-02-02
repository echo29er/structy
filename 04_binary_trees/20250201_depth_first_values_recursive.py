class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_first_values (root: Node) -> list:
    """
    Function Purpose: 
        Write a function, depth_first_values, that takes in the root of a binary tree. 
        The function should return a list containing all values of the tree in depth-first order.

    Args:
        root (Node): the root of the binary tree.

    Returns:
        list: containing all values of the tree in depth-first order. 

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - Node values can be of any type that can be stored in a list

    Time complexity: 
        O(n²) where n is number of nodes because:
        - We visit each node once O(n)
        - BUT at each node, we perform list concatenation using the * operator
        - List concatenation creates a new list and copies elements, which is O(m) where m is list size
        - As we go up the tree, these lists get bigger, up to size O(n)
        - Therefore, we're doing O(n) operations n times = O(n²)

    Space complexity: 
        O(n) where n is the number of nodes in the tree:
        - O(n) for the result list which must store all node values
        - O(n) worst case for the stack (skewed tree)
        - O(log n) best case for the stack (balanced tree)
    """

    ## RECURSIVE SOLUTION
    # The recursive solution leverages the call stack instead of an explicit stack
    # Base case: empty node returns empty list
    # Recursive case: 
    #   1. Get values from left subtree recursively
    #   2. Get values from right subtree recursively
    #   3. Combine current node value with left and right values using list unpacking (this is expensive!)
    #      Each time we unpack and concatenate lists, we create a new list and copy elements
    # Pre-order traversal is achieved by processing root before recursive calls

    # Base case we have an empty root
    if root is None: 
        return []
        
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    
    return [root.val, *left_values, *right_values] # * operator unpacks the lists


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

    return depth_first_values(a)
    #   -> ['a', 'b', 'd', 'e', 'c', 'f']

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

    return depth_first_values(a)
    #   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

def test_c():
    a = Node('a')
    #     a
    return depth_first_values(a) 
    #   -> ['a']

def test_d():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    a.right = b
    b.left = c
    c.right = d
    d.right = e

    #      a
    #       \
    #        b
    #       /
    #      c
    #       \
    #        d
    #         \
    #          e

    return depth_first_values(a) 
    #   -> ['a', 'b', 'c', 'd', 'e']

def test_e():
    return depth_first_values(None) 
    #   -> []


print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())