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
        - We still visit each node exactly once
        - At each node, we do constant time operations (just addition)
        - So total time is proportional to number of nodes

    Space complexity: 
        O(h) where h is height of tree
        - This is different from our iterative solution!
        - Each recursive call adds a frame to the call stack
        - Maximum depth of recursion equals height of tree
        - Best case (balanced tree): O(log n)
        - Worst case (skewed tree): O(n)
    """

    ## RECURSIVE APPROACH
    # The recursive solution leverages the call stack instead of an explicit stack
    # Base case: empty node returns empty list
    # Recursive case: 
    #   1. Get values from left subtree recursively
    #   2. Get values from right subtree recursively
    #   3. Combine current node value with left and right values using list unpacking (this is expensive!)
    #      Each time we unpack and concatenate lists, we create a new list and copy elements
    # Pre-order traversal is achieved by processing root before recursive calls

    # Instantiate the list and the stack
    # Base case we have an empty root
    if root is None: 
        return 0
        
    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)
    
    return root.val + left_sum + right_sum 

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