from typing import Union

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_includes (root: Node, target: Union[str, int]) -> bool:
    """
    Function Purpose: 
        Write a function, tree_includes, that takes in the root of a binary tree and a target value. 
        The function should return a boolean indicating whether or not the value is contained in the tree.

    Args:
        root (Node): the root of the binary tree.

    Returns:
        bool: If the target value exists in the tree. 

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - Node values are all positive or negative integers. 

    Time complexity: 
        O(n) where n is number of nodes because:
        - We may visit each node  nce

    Space complexity: 
        O(n) where n is the number of nodes in the tree:
        - O(n) for storing nodes in our queue list
    """

     ## ITERATIVE APPROACH USING STACK
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree
    # This can use either depth first or breadth first.
    # We use depth-first traversal with a stack (LIFO)
    # This processes all nodes in a branch before moving to siblings

    # We start by instantiating a stack to traverse the tree. 
    # If we have an empty binary tree then that is still a valid binary tree and we return False. 
    # If the root is not empty then we add the node to the stack. 
    # The stack allows us to work Last in First out (LiFo). 
    # We want to add each node's children, from right to left, to the stack to maintain LiFo.
    # We pop the last element in the stack.

    # Instantiate stack
    stack = [] # stack. 

    # Base case we have an empty root
    if root is None: 
        return False
    else: 
        stack.append(root) # Add the root to the stack
        
    while stack: # While we still have nodes to process
        current = stack.pop()
        if current.val == target: 
            return True # returning true exits the program

        if current.right is not None: # We must add the right child first to maintain LiFO.
            stack.append(current.right)
        if current.left is not None: 
            stack.append(current.left) # We add the left child second so that it is processed first (LiFo).
        # Add children in right-left order for depth-first traversal
    
    return False # If none of the values in the queue i.e. from the tree match the target then return False

def test_a():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

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

    return tree_includes(a, "e") # -> True

def test_b():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

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
    return tree_includes(a, "a") # -> True

def test_c ():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

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

    return tree_includes(a, "n") # -> False

def test_d ():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

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

    return tree_includes(a, "f") # -> True

def test_e ():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

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

    return tree_includes(a, "p") # -> False

def test_f ():
    return tree_includes(None, "b") # -> False


print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
print(test_f())