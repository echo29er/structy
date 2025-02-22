from typing import Union

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bottom_right_value (root: Node) -> Union[int, str]:
    """
    Function Purpose: 
        Write a function, bottom_right_value, that takes in the root of a binary tree. 
        The function should return the right-most value in the bottom-most level of the tree.

    Parameters:
        root (Node): the root of the binary tree.

    Returns:
        Union[int, str]: The value at the right-most and bottom-most level of the tree.
        
    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - You may assume that the input tree is non-empty

    Time complexity: 
        O(n) where n is the number of nodes in the tree, as we have to visit each node in the tree. 

    Space Complexity: O(n) where n is the number of nodes in the tree.

    """

    ## RECURSIVE 
    # Our base case is one node

    # We need to track both max depth and the value we want
    result = {'max_depth': -1, 'value': None}
    
    def dfs(node, depth):
        if not node:
            return
            
        # If we're at a deeper level OR this is the first node we've seen
        if depth > result['max_depth']:
            result['max_depth'] = depth
            result['value'] = node.val
            
        # Go right first to find rightmost nodes at each level
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    
    dfs(root, 0)
    return result['value']
    
    
def test_a():
    a = Node(3)
    b = Node(11)
    c = Node(10)
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
    #   11     10
    #  / \      \
    # 4   -2     1

    return bottom_right_value(a) # -> 1

def test_b():
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \       
    #    -2  6

    return bottom_right_value(a) # -> 6

def test_c():
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)
    i = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \    /   
    #    -2  6  7 

    return bottom_right_value(a) # -> 7

def test_d():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.right = d
    d.left = e
    e.right = f

    #      a
    #    /   \ 
    #   b     c
    #    \
    #     d
    #    /
    #   e
    #   \
    #    f
            
    return bottom_right_value(a) # -> 'f'

def test_e():
    a = Node(42)

    #      42

    return bottom_right_value(a) # -> 42

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())