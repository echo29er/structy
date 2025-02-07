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
        O(n) where n is the number of nodes in the tree:
        - O(n) for storing nodes in our stack
    """

    ## ITERATIVE APPROACH USING STACK
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree.
    # We can use either depth first or breadth first.
    # We will use depth first in this configuration. 

    # We start by instantiating a stack to traverse the tree.  
    # The tree is assumed to never be empty.  
    # The stack allows us to work Last in First out (LiFo). 
    # We want to add each node's children to the stack to maintain LiFo.
    # To traverse the list, we pop the stack. 
    # We then add the node's right child node then left child node to the stack so that we pop the left before the right.
    # This is important as the queue is Last In First Out.

    # Instantiate  the stack
    stack = [] # stack.

    stack.append(root) # Add the root to the queue

    # We'll use the guess and check pattern. Where we'll assume the first value is the smallest and compare it with each subsequent.
    smallest_value = root.val
        
    while stack: # While there are values in the stack
        current = stack.pop()
        if current.val < smallest_value: 
            smallest_value = current.val

        if current.right is not None: # We must add the right child first to the stack so it is processed after the left node and its children.
            stack.append(current.right)
        if current.left is not None: 
            stack.append(current.left) # We add the left child second so that it is processed first (LiFo).
        # Add children in right-left order for depth-first traversal
    
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