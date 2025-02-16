class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_value_count (root: Node, target: int) -> int:
    """
    Function Purpose: 
        Write a function, tree_value_count, that takes in the root of a binary tree and a target value. 
        The function should return the number of times that the target occurs in the tree.

    Parameters:
        root (Node): the root of the binary tree.
        target: int value to find in the tree.

    Returns:
        int: The count of the number of times the target appears in the tree. 
        
    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)

    Time complexity: 
        O(n) where n is the number of nodes in the tree, as we may need to visit each node exactly once
        during the breadth-first traversal.

    Space Complexity: O(w) where w is the maximum width of the tree:
        - O(n) in worst case, where n is the number of nodes
        (in a complete binary tree, the bottom level contains up to n/2 nodes)
        - Still O(n) for a balanced tree, as the maximum width is still n/2

    """

    ## ITERATIVE APPROACH USING QUEUE DUE TO BREADTH FIRST TRAVERSAL
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree.
    # As we need to count all the nodes that have the same value as the target, we can use either depth first traversal or breadth first traveral.
    # We will need to visit all the nodes in the tree to return the count.
    # As we visit a node, we will not need to keep any additional data, i.e. a path, as we're just interested in the count. 

    # For breadth first traversal, we start by instantiating a queue to traverse the tree. 
    # The queue allows us to work First in First out (FiFo). 
    # We add the children in left to right order to the queue to maintain FiFo.
    # If we pop the first element of the queue then we would have suffer from O(n^2) time complexity due to the need to move all the elements leftwards in the queue. 
    # To avoid this, we can use a pointer, and use that to traverse the queue. 

    # Base case: Root is None
    if root is None: 
        return 0

    # Instantiate and initalise the queue, the pointer for traversal, and the count
    queue = [root] # node
    pointer = 0 # start at the first index
    count = 0 

        
    while pointer < len(queue) : # While we still have elements to process
        # Get the current node and check its value against target. 
        current_node = queue[pointer]
        
        if current_node.val == target:
            count += 1
        
        # If not a leaf, then add children to the stack.
        if current_node.left is not None: 
            # We add the left child first as it is processed first in the queue i.e. we're working FiFo.
            queue.append(current_node.left) # append the left node
        if current_node.right is not None: 
            # We add the right child second so it is processed second i.e. FiFo
            queue.append(current_node.right) # append the right node
        # Add children in left-right order for breadth-first traversal

        pointer += 1 # move the pointer
    
    # If the target is never found in the tree then return 0.
    return count

def test_a():
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   6     6
    #  / \     \
    # 4   6     12

    return tree_value_count(a,  6) # -> 3

def test_b():
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   6     6
    #  / \     \
    # 4  6     12

    return tree_value_count(a,  12) # -> 2

def test_c ():
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      7
    #    /   \
    #   5     1
    #  / \     \
    # 1   8     7
    #    /       \
    #   1         1

    return tree_value_count(a, 1) # -> 4

def test_d ():
    a = Node(7)
    b = Node(5)
    c = Node(1)
    d = Node(1)
    e = Node(8)
    f = Node(7)
    g = Node(1)
    h = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      7
    #    /   \
    #   5     1
    #  / \     \
    # 1   8     7
    #    /       \
    #   1         1

    return tree_value_count(a, 9) # -> 0

def test_e():
    return tree_value_count(None, 42) # -> 0

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
