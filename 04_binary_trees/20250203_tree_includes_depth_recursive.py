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

    Parameters:
        root (Node): the root of the binary tree.
        target: value to find in the tree.

    Returns:
        bool: If the target value exists in the tree. 

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - Node values can be of any type that can be compared for equality with target

    Time complexity: 
        O(n) where n is number of nodes because:
        - We may visit each node once

    Space complexity: 
        O(h) where h is height of tree
        - This is different from our iterative solution!
        - Each recursive call adds a frame to the call stack
        - Maximum depth of recursion equals height of tree
        - Best case (balanced tree): O(log n)
        - Worst case (skewed tree): O(n)
    """

    ## RECURSIVE APPROACH
    # Base case: empty node returns 0
    # For each node:
    #   - Count current node (1 if matches target, 0 if not)
    #   - Add counts from left and right subtrees recursively
    # Return total count

    # Base case we have an empty root
    if root is None: 
        return False
    
    if root.val == target: 
        return True
    
    return tree_includes(root.left, target) or tree_includes(root.right,target)
    

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