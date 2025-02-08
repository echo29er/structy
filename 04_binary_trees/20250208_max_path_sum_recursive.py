class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum (root: Node) -> int:
    """
    Function Purpose: 
        Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. 
        The function should return the maximum sum of any root to leaf path within the tree.

    Args:
        root (Node): the root of the binary tree.

    Returns:
        int: The maximum sum of any root to leaf path within tree.

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - Node values are all positive or negative integers. 
        - You may assume that the input tree is non-empty.

    Time complexity: 
        O(n) where n is the number of nodes in the tree, as we visit each node exactly once
        during the depth-first traversal.

    Space complexity: 
        O(h) where h is the height of the tree:
        - In a balanced tree, h = log(n)
        - In a completely unbalanced tree (essentially a linked list), h = n
        The space is used for the stack storing (node, path_sum) pairs during traversal.
    """

    ## RECURSIVE APPROACH
    # Base case 1: if node doesn't exist, return negative infinity
    # This ensures this path won't be chosen as the maximum
    if root is None:
        return float('-inf')

    # Base case 2: if we're at a leaf node, return its value
    if root.left is None and root.right is None: 
        return root.val
    
    # Get the maximum path sum from left and right subtrees
    # If a subtree doesn't exist, it will return negative infinity
    left_sum = max_path_sum(root.left)
    right_sum = max_path_sum(root.right)

    return root.val + max(left_sum, right_sum)

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

    return max_path_sum(a) # -> 18

def test_b():
    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \      
    # 20   15
    #      / \
    #     1  3

    return max_path_sum(a) # -> 59

def test_c ():
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(-13)
    g = Node(-1)
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
    # -3   0    -13
    #     /       \
    #    -1       -2

    return max_path_sum(a) # -> -8

def test_d ():
    a = Node(42)

    #        42

    return max_path_sum(a) # -> 42


print(test_a())
print(test_b())
print(test_c())
print(test_d())