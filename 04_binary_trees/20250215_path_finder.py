from typing import Union

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_finder (root: Node, target: Union[str, int]) -> list:
    """
    Function Purpose: 
        Write a function, path_finder, that takes in the root of a binary tree and a target value. 
        The function should return an array representing a path to the target value. 
        If the target value is not found in the tree, then return None.

    Args:
        root (Node): the root of the binary tree.

    Returns:
        list: the path to the target value from the root.

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - You may assume that the input tree is non-empty.
        - You may assume that the tree contains unique values.

    Time complexity: 
        O(n) where n is the number of nodes in the tree, as we may need to visit each node exactly once
        during the depth-first traversal.

    Space complexity: 
        O(h²) because:
        - The stack itself uses O(h) space
        - Each element in the stack contains a path list of up to length h
        - Total: O(h) elements x O(h) size per path = O(h²)

        Worst case (unbalanced tree): h = n, so space complexity is O(n²)
        Best case (balanced tree): h = log(n), so space complexity is O(log²(n))

    Initial thoughts
        We should be able to reuse the tuple logic to construct a chain. 

    """

    ## ITERATIVE APPROACH USING STACK DUE TO DEPTH FIRST TRAVERSAL
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree.
    # As we want to find a path from root to leaf, we will need to use depth first traversal.
    # We may need to visit all nodes in the tree.
    # As we visit a node, we will need to keep a track of the preceding nodes visited. We can add this as a list in a tuple that we add to the stack in the format (node, [path_so_far]) 

    # For depth first traversal, we start by instantiating a stack to traverse the tree. 
    # The tree is assumed to never be empty.
    # The stack allows us to work Last in First out (FiFo). 
    # We add the children in right to left order to the stack to maintain LiFo.
    # We Pop the first element in the stack to give us depth traversal.
    # What's new about this situation is that we need to sum each branch.

    # Base case: Root is None
    if root is None: 
        return None

    # Instantiate and initalise the stack
    stack = [(root, [root.val])] # Add the root node and it's value to the stack
        
    while stack: # While we still have elements to process
        # Get the current node and path up to this node
        current_node, current_path = stack.pop()

        if current_node.val == target:
            return current_path

        # If not a leaf, then add children to the stack.
        if current_node.right is not None: 
            # We add the right child first as it is processed later in the stack i.e. we're working LiFo.
            # We also add the current child's value to the current path sum
            stack.append((current_node.right, current_path + [current_node.right.val])) # We create a new list for each path by using current_path + [current_node.right.val] instead of modifying the original list in place. 
        if current_node.left is not None: 
            # We add the left child second so it is popped first i.e. LiFo
            stack.append((current_node.left, current_path + [current_node.left.val]))
        # Add children in right-left order for order for depth-first traversal
    
    # If the target is never found in the tree then return None.
    return None

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

    return path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]

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

    return path_finder(a, 'p') # -> None

def test_c ():
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

    return path_finder(a, "c") # -> ['a', 'c']

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

    return path_finder(a, "h") # -> ['a', 'c', 'f', 'h']

def test_e():
    x = Node("x")

    #      x

    return path_finder(x, "x") # -> ['x']

def test_f():
    path_finder(None, "x") # -> None

def test_g(): 
    root = Node(0)
    curr = root
    for i in range(1, 19500):
        curr.right = Node(i)
        curr = curr.right

        #      0
        #       \
        #        1
        #         \
        #          2
        #           \
        #            3
        #             .
        #              .
        #               .
        #              19498
        #                \
        #                19499

    return path_finder(root, 16281) # -> [0, 1, 2, 3, ..., 16280, 16281]

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
print(test_f())
print(test_g())