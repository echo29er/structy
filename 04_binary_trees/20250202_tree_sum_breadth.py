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
        - O(n) for storing nodes in our queue list
    """

    ## ITERATIVE APPROACH USING QUEUE
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree
    # This can use either depth first or breadth first.
    # We will re-use breadth first here. 

    # We start by instantiating a queue "branch_traversal" to traverse the tree, and an integer "tree_sum_result"=0 to add our values to. 
    # If we have an empty binary tree then that is still a valid binary tree and we return "tree_sum_result". 
    # If the root is not empty then we add the node to "branch_traversal". 
    # The queue allows us to work First in First out (FiFo). 
    # We want to add each node's children to the end of the queue to maintain FiFo.
    # If we Pop the first element in the list then the list needs to be reconstructed; therefore we can keep the list intact
    # by instead using a pointer to traverse the list. 
    # We then add the node's left child node then right child node to the queue.
    # This is important as the queue is First In First Out.

    # Instantiate the list and the queue
    tree_sum_result = 0
    branch_traversal = [] # queue. Instead of introducing collections deque, we can use a pointer.

    # Base case we have an empty root
    if root is None: 
        return tree_sum_result
    else: 
        branch_traversal.append(root) # Add the root to the queue
        branch_traversal_pointer = 0 # Using list as queue with pointer to avoid O(n) pop(0) operations
        
    while branch_traversal_pointer < len(branch_traversal): # While we still have elements to process
        current = branch_traversal[branch_traversal_pointer] 
        tree_sum_result += current.val # Add the popped node's value to the list. 

        if current.left is not None: # We must add the left child first as we add to the end of the queue.
            branch_traversal.append(current.left)
        if current.right is not None: 
            branch_traversal.append(current.right) # We add the right child second so that it is processed first (FiFo).
        # Add children in left-right order for level-by-level traversal
        
        branch_traversal_pointer += 1 # move the pointer
    
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