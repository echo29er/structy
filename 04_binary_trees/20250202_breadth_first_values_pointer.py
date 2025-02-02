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
        list: containing all values of the tree in breadth-first order. 

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - Node values can be of any type that can be stored in a list

    Time complexity: 
        O(n) where n is number of nodes because:
        - We visit each node exactly once
        - Using a pointer approach means we get O(1) access to the "front" element
        - If we had used pop(0) instead, it would be O(n²) due to shifting elements

    Space complexity: 
        O(n) where n is the number of nodes in the tree:
        - O(n) for the result list which must store all node values
        - O(n) worst case for the queue (skewed tree)
        - O(log n) best case for the queue (balanced tree)
    """

    ## ITERATIVE APPROACH USING QUEUE
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree
    # This implementation utilises a queue, where we work First in First out. 
    # The space complexity is O(n) for both the queue and result list

    # We start by instantiating a queue to traverse the tree, and a list to add our final values to. 
    # If we have an empty binary tree then that is still a valid binary tree and we return an empty list. 
    # If the root is not empty then we add the node to the queue. 
    # When we have a queue, we can then start saving values. 
    # We traverse the branch by popping the first node of the queue, and appending its value to the end of the queue.
    # FYI as popping the front of the queue requires shifting each element to the left once, we need to either use
    # Collections deque, or we can use a pointer. here we will use a pointer.  
    # We then add the node's left child node then right child node to the queue.
    # This is important as the queue is First In First Out.

    # Instantiate the list and the queue
    visited_nodes_values = []
    branch_traversal = [] # queue. Instead of introducing collections deque, we can use a pointer.

    # Base case we have an empty root
    if root is None: 
        return []
    else: 
        branch_traversal.append(root) # Add the root to the queue
        branch_traversal_pointer = 0 # Using list as queue with pointer to avoid O(n) pop(0) operations
        
    while branch_traversal_pointer < len(branch_traversal): # While we still have elements to process
        current = branch_traversal[branch_traversal_pointer] # 
        visited_nodes_values.append(current.val) # Add the popped node's value to the list. 

        if current.left is not None: # We must add the left child first as we add to the end of the queue.
            branch_traversal.append(current.left)
        if current.right is not None: 
            branch_traversal.append(current.right) # We add the right child second so that it is processed first (FiFo).
        # Add children in left-right order for level-by-level traversal
        
        branch_traversal_pointer += 1 # move the pointer
    
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