from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def breadth_first_values (root: Node) -> list:
    """
    Function Purpose: 
        Write a function, breadth_first_values, that takes in the root of a binary tree. 
        The function should return a list containing all values of the tree in breadth-first order.

    Args:
        root (Node): the root of the binary tree.

    Returns:
        list: containing all values of the tree in breadth-first order (level by level). 

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - Node values can be of any type that can be stored in a list

    Time complexity: 
        O(n) we must visit every node in the tree exactly once, with O(1) queue operations using deque. 

    Space complexity: 
        O(n) where n is the number of nodes in the tree:
        - O(n) for the result list which must store all node values
        - O(n) worst case for the queue (skewed tree)
        - O(log n) best case for the queue (balanced tree)
    """

    ## ITERATIVE APPROACH USING DEQUE AS QUEUE (DEQUE is a doubly-linked list hence we can pop at the start or end)
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree
    # This implementation uses a deque as a queue, where we work First In First Out (FIFO)
    # We use collections.deque instead of a list because:
    #   - deque provides O(1) operations at both ends
    #   - using list.pop(0) would be O(n) as it requires shifting all elements left
    # The space complexity is O(n) for both the queue and result list

    # Instantiate the list and the queue
    visited_nodes_values = []
    branch_traversal = deque() # Using deque for efficient queue operations

    # Base case we have an empty root
    if root is None: 
        return []
    else: 
        branch_traversal.append(root) # Add the root to the queue
        
    while branch_traversal: # While the list has nodes
        current = branch_traversal.popleft() # Traverse the branch by taking the first element.
        visited_nodes_values.append(current.val) # Add the popped node's value to the list. 

        if current.left is not None: # We must add the left child first as we add to the end of the queue.
            branch_traversal.append(current.left)
        if current.right is not None: 
            branch_traversal.append(current.right) # We add the right child second so that it is processed first (FiFo).
    
    return visited_nodes_values

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

    return breadth_first_values(a) 
    #    -> ['a', 'b', 'c', 'd', 'e', 'f']

def test_b():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    return breadth_first_values(a) 
    #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def test_c():
    a = Node('a')

    #      a

    return breadth_first_values(a) 
    #    -> ['a']

def test_d():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    x = Node('x')

    a.right = b
    b.left = c
    c.left = x
    c.right = d
    d.right = e

    #      a
    #       \
    #        b
    #       /
    #      c
    #    /  \
    #   x    d
    #         \
    #          e

    return breadth_first_values(a) 
    #    -> ['a', 'b', 'c', 'x', 'd', 'e']

def test_e():
    return breadth_first_values(None) 
    #    -> []

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())