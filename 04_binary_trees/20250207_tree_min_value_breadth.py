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
        - O(n) for storing nodes in our queue list
    """

    ## ITERATIVE APPROACH USING QUEUE
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree.
    # We can use either depth first or breadth first.
    # We will use breadth first in this configuration. 

    # We start by instantiating a queue to traverse the tree. 
    # The tree is assumed to never be empty.
    # The queue allows us to work First in First out (FiFo). 
    # We want to add each node's children to the end of the queue to maintain FiFo.
    # If we Pop the first element in the list then the list needs to be reconstructed; therefore we can keep the list intact
    # by instead using a pointer to traverse the list. 
    # We then add the node's left child node then right child node to the queue.
    # This is important as the queue is First In First Out.

    # Instantiate  the queue
    queue = [] # queue. Instead of introducing collections deque, we can use a pointer.

    queue.append(root) # Add the root to the queue
    pointer = 0 # Using list as queue with pointer to avoid O(n) pop(0) operations

    # We'll use the guess and check pattern. Where we'll assume the first value is the smallest and compare it with each subsequent.
    smallest_value = root.val
        
    while pointer < len(queue): # While we still have elements to process
        current = queue[pointer] 
        if current.val < smallest_value: 
            smallest_value = current.val

        if current.left is not None: # We must add the left child first as we add to the end of the queue.
            queue.append(current.left)
        if current.right is not None: 
            queue.append(current.right) # We add the right child second so that it is processed first (FiFo).
        # Add children in left-right order for level-by-level traversal
        
        pointer += 1 # move the pointer
    
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