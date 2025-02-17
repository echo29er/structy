class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def how_high (root: Node) -> int:
    """
    Function Purpose: 
        Write a function, how_high, that takes in the root of a binary tree. 
        The function should return a number representing the height of the tree.

        The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

        If the tree is empty, return -1.

    Parameters:
        root (Node): the root of the binary tree.

    Returns:
        int: The height of the tree i.e. the maximal number of edges from the root node to any leaf node. 
        
    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)

    Time complexity: 
        O(n) where n is the number of nodes in the tree, as we have to visit each node in the tree. 

    Space Complexity: O(h) where h is height of the tree
        - O(h) for a skewed tree
        - O(log(n)) for a balance tree

    """

    ## ITERATIVE APPROACH USING STACK DUE TO DEPTH FIRST TRAVERSAL
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree.
    # As we are dealing with the depth of the tree, we will need to use depth first search. 
    # We will need to visit all the nodes in the tree to return maximum height.
    # As we visit a node, we will need to keep a track of the height. 

    # For depth first traversal, we instantiate and initialise a stack. 
    # The stack allows us to consider nodes Last in First Out.
    # We add the children in right to left order to maintain LiFo.
    # We pop the stack so that we're working with the most recently added node i.e. the left node we added.
    # We need to determine when we have a hit the end of a branch; therefore we need to program for: 
    # 1) an empty tree, 2) a branch with no children i.e. we've hit the end of a branch, 3) a branch with right children (first so they're added to the stack first), 4) a branch with left children so 
    # they're added second but actually processed first. 
    # We'll need to track the current_count of a branch and a max_count referring to the maximal number of edges. We can then compare these and return max_count at the end. 

    # Base case: Root is None
    if root is None: 
        return -1

    # Instantiate and initalise the stack, and max_count
    current_path_count = 0 # We know we have one node therefore both current_count and max_count are set to 0 i.e. the number of edges
    stack = [(root, current_path_count)] # node, count of nodes in the branch
    max_count = 0 
        
    while stack: # While we still have elements to process
        # Get the current node. 
        current_node, current_path_count = stack.pop()
        
        # When this is the end of a branch i.e. a leaf node then we've complete a path. 
        # We then compare current_count with max_count and assign the value of the max between the two to max_count.
        if current_node.left is None and current_node.right is None: 
            max_count = max(max_count, current_path_count)
        
        # If not a leaf, then add children to the stack.
        if current_node.right is not None: 
            # We add the right child first to process it after the left child and maintain LiFo.
            stack.append((current_node.right, current_path_count + 1)) # append the right node
        if current_node.left is not None: 
            # We add the left child second so it is processed first for LiFo
            stack.append((current_node.left, current_path_count + 1)) # append the left node
        # Add children in right-left order for depth-first traversal
    
    return max_count

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

    return how_high(a) # -> 2

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

    return how_high(a) # -> 3

def test_c ():
    a = Node('a')
    c = Node('c')

    a.right = c

    #      a
    #       \
    #        c

    return how_high(a) # -> 1

def test_d ():
    a = Node('a')

    #      a

    return how_high(a) # -> 0

def test_e():
    return how_high(None) # -> -1


print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())