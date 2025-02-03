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

    ## ITERATIVE APPROACH USING QUEUE
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree
    # This can use either depth first or breadth first.
    # We will re-use breadth first here. 

    # We start by instantiating a queue to traverse the tree. 
    # If we have an empty binary tree then that is still a valid binary tree and we return "tree_sum_result". 
    # If the root is not empty then we return False. 
    # The queue allows us to work First in First out (FiFo). 
    # We want to add each node's children to the end of the queue to maintain FiFo.
    # If we Pop the first element in the list then the list needs to be reconstructed; therefore we can keep the list intact
    # by instead using a pointer to traverse the list. 
    # We then add the node's left child node then right child node to the queue.
    # This is important as the queue is First In First Out.

    # Instantiate  the queue
    queue = [] # queue. Instead of introducing collections deque, we can use a pointer.


    # Base case we have an empty root
    if root is None: 
        return False
    else: 
        queue.append(root) # Add the root to the queue
        pointer = 0 # Using list as queue with pointer to avoid O(n) pop(0) operations
        
    while pointer < len(queue): # While we still have elements to process
        current = queue[pointer] 
        if current.val == target: 
            return True # returning true exits the program

        if current.left is not None: # We must add the left child first as we add to the end of the queue.
            queue.append(current.left)
        if current.right is not None: 
            queue.append(current.right) # We add the right child second so that it is processed first (FiFo).
        # Add children in left-right order for level-by-level traversal
        
        pointer += 1 # move the pointer
    
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