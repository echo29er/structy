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
        O(n) we must visit every node in the tree exactly once. 

    Space complexity: 
        O(n) where n is the number of nodes in the tree:
        - O(n) for the result list which must store all node values
        - O(n) worst case for the stack (skewed tree)
        - O(log n) best case for the stack (balanced tree)
    """

    ## ITERATIVE APPROACH USING STACK
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree
    # This implementation uses pre-order traversal (process node, then left subtree, then right subtree)
    # The space complexity is O(n) for both the stack and result list

    # We start by instantiating a stack to traverse the tree, and a list to add our final values to. 
    # If we have an empty binary tree then that is still a valid binary tree and we return an empty list. 
    # If the root is not empty then we add the node to the stack. 
    # When we have a stack, we can then start saving values. 
    # We traverse the branch by popping the node of the stack, and adding its value to the list. 
    # We then  add the node's right child node then left child node to the stack.
    # This is important as the stack is Last In First Out therefore we want to process the left child first.

    # Instantiate the list and the stack
    visited_nodes_values = []
    branch_traversal = [] # stack

    # Base case we have an empty root
    if root is None: 
        return []
    else: 
        branch_traversal.append(root) # Add the root to the stack
        
    while branch_traversal: # While the list has nodes
        current = branch_traversal.pop() # Traverse the branch by taking the top of the stack
        visited_nodes_values.append(current.val) # Add the popped node's value to the list. 

        if current.right is not None: # We must add the right child first so that it is processed after the left
            branch_traversal.append(current.right)
        if current.left is not None: 
            branch_traversal.append(current.left) # We add the left child second so that it is processed first (LiFo).
    
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