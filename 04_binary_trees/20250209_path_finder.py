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
        int: The maximum sum of any root to leaf path within tree.

    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - You may assume that the input tree is non-empty.
        - You may assume that the tree contains unique values.

    Time complexity: 
        O(n) where n is the number of nodes in the tree, as we may need to visit each node exactly once
        during the depth-first traversal.

    Space complexity: 
        O(h) where h is the height of the tree:
        - In a balanced tree, h = log(n)
        - In a completely unbalanced tree (essentially a linked list), h = n
        The space is used for the stack storing (node, path_sum) pairs during traversal.

    Initial thoughts
        We should be able to reuse the tuple logic to construct a chain. 

    """

    ## ITERATIVE APPROACH USING STACK DUE TO DEPTH FIRST TRAVERSAL
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree.
    # As we want to find the sum of each root to leaf, we will need to use depth first traversal.
    # We will need visit each node in each branch in order to understand its sum for comparison. 
    # We can guess that the first root to leaf branch contains the maximum_sum, and compare each remaining root to leaf branch with that. 
    # Where a subsequent root to leaf branch sum is greater we can assign maximum_sum with its value. 

    # For depth first traversal, we start by instantiating a stack to traverse the tree. 
    # The tree is assumed to never be empty.
    # The stack allows us to work Last in First out (FiFo). 
    # We add the children in right to left order to the stack to maintain LiFo.
    # We Pop the first element in the stack to give us depth traversal.
    # What's new about this situation is that we need to sum each branch.

    # Instantiate and initalise the stack
    stack = [(root, root.val)] # Add the root node and it's value to the stack

    # Initialise a maximum_sum to negative infinity for comparison
    maximum_sum = float('-inf')
        
    while stack: # While we still have elements to process
        # Get the current node and the sum of the path up to this node
        current_node, current_path_sum = stack.pop()

        # When this is a leaf node i.e. it has no children, then we've completed a path. 
        # Compare its path sum with our current maximum, and assign maximum_sum to the greater of the two. 
        if current_node.left is None and current_node.right is None:
            maximum_sum = max(maximum_sum, current_path_sum)

        # If not a leaf, then add children to the stack.
        if current_node.right is not None: 
            # We add the right child first as it is processed later in the stack i.e. we're working LiFo.
            # We also add the current child's value to the current path sum
            stack.append((current_node.right, current_path_sum + current_node.right.val))
        if current_node.left is not None: 
            # We add the left child second so it is popped first i.e. LiFo
            stack.append((current_node.left, current_path_sum + current_node.left.val)) 
        # Add children in right-left order for order for depth-first traversal
    
    return maximum_sum

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

    return max_path_sum(a) # -> 18

def test_b():
    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \      
    # 20   15
    #      / \
    #     1  3

    return max_path_sum(a) # -> 59

def test_c ():
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(-13)
    g = Node(-1)
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
    # -3   0    -13
    #     /       \
    #    -1       -2

    return max_path_sum(a) # -> -8

def test_d ():
    a = Node(42)

    #        42

    return max_path_sum(a) # -> 42


print(test_a())
print(test_b())
print(test_c())
print(test_d())