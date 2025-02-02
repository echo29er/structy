class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_sum (root: Node) -> int:
    """
    Function Purpose: 
        Write a function, tree_sum, that takes in the root of a binary tree that contains number values. 
        The function should return the total sum of all values in the tree.

    Args:
        root (Node): the root of the binary tree.

    Returns:
        int: The sum of all the values of each Node in the tree. 

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - Node values are all positive or negative integers. 

    Time complexity: 
        O(n) where n is number of nodes because:
        - We visit each node exactly once
        - Each operation (accessing value, adding children) is O(1)

    Space complexity: 
        O(n) where n is the number of nodes in the tree:
        - O(n) for storing nodes in our stack list
    """

    ## ITERATIVE APPROACH USING STACK
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree
    # This can use either depth first or breadth first.
    # We use depth-first traversal with a stack (LIFO)
    # This processes all nodes in a branch before moving to siblings

    # We start by instantiating a stack to traverse the tree, and an integer "tree_sum_result"=0 to add our values to. 
    # If we have an empty binary tree then that is still a valid binary tree and we return "tree_sum_result". 
    # If the root is not empty then we add the node to the stack. 
    # The stack allows us to work Last in First out (LiFo). 
    # We want to add each node's children, from right to left, to the stack to maintain LiFo.
    # We pop the last element in the stack .

    # Instantiate the list and the stack
    tree_sum_result = 0
    stack = [] # stack. 

    # Base case we have an empty root
    if root is None: 
        return tree_sum_result
    else: 
        stack.append(root) # Add the root to the stack
        
    while stack: # While there are elements in the stack
        current = stack.pop() # take the first element off the stack
        tree_sum_result += current.val # Add the popped node's value to the list. 

        if current.right is not None: # We must add the right child first to maintain LiFo.
            stack.append(current.right)
        if current.left is not None: 
            stack.append(current.left) # We add the left child second so that it is processed first (LiFo).
        # Add children in right-left order for depth-first traversal
    
    return tree_sum_result

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

    return tree_sum(a) # -> 21

def test_b():
    a = Node(1)
    b = Node(6)
    c = Node(0)
    d = Node(3)
    e = Node(-6)
    f = Node(2)
    g = Node(2)
    h = Node(2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      1
    #    /   \
    #   6     0
    #  / \     \
    # 3   -6    2
    #    /       \
    #   2         2

    return tree_sum(a) # -> 10 

def test_c ():
    return tree_sum(None) # -> 0


print(test_a())
print(test_b())
print(test_c())