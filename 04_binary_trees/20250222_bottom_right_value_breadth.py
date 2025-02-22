from typing import Union

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bottom_right_value (root: Node) -> Union[int, str]:
    """
    Function Purpose: 
        Write a function, bottom_right_value, that takes in the root of a binary tree. 
        The function should return the right-most value in the bottom-most level of the tree.

    Parameters:
        root (Node): the root of the binary tree.

    Returns:
        Union[int, str]: The value at the right-most and bottom-most level of the tree.
        
    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - You may assume that the input tree is non-empty

    Time complexity: 
        O(n) where n is the number of nodes in the tree, as we have to visit each node in the tree. 

    Space Complexity: O(n) where n is the number of nodes in the tree.

    """

    ## ITERATIVE APPROACH USING QUEUE DUE TO BREADTH FIRST TRAVERSAL
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree.

    # We can use breadth first search with a queue. The last node in the queue will be the right most node: 
    # it will be processed last. 

    # For breadth first traversal, we instantiate and initialise a queue. 
    # The queue allows us to consider nodes First in First Out.
    # We add the children in left to right order to maintain FiFo.
    # We use a pointer to traverse the queue, as if we were to pop the start of the queue then we would add
    # time complexity by having to adjust the queue. 
    # We have been told that the tree will not be empty. 
    # We need to determine when we have a hit the end of a branch; therefore we need to program for: 
    # We will process each branch from breadth first from left to right. 

    # Instantiate and initialise the queue and the pointer
    queue = [root]
    pointer = 0

    # While the queue has values. 
    while pointer < len(queue): 
        current_node = queue[pointer]
        last_node_value = current_node.val
            
        # If not a leaf, then add the left child to the queue to maintain FiFo:
        if current_node.left is not None: 
            queue.append(current_node.left)
        # Then add the right child so that that is processed first
        if current_node.right is not None: 
            queue.append(current_node.right)
        
        pointer += 1

    return last_node_value

def test_a():
    a = Node(3)
    b = Node(11)
    c = Node(10)
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
    #   11     10
    #  / \      \
    # 4   -2     1

    return bottom_right_value(a) # -> 1

def test_b():
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \       
    #    -2  6

    return bottom_right_value(a) # -> 6

def test_c():
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)
    i = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \    /   
    #    -2  6  7 

    return bottom_right_value(a) # -> 7

def test_d():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.right = d
    d.left = e
    e.right = f

    #      a
    #    /   \ 
    #   b     c
    #    \
    #     d
    #    /
    #   e
    #   \
    #    f
            
    return bottom_right_value(a) # -> 'f'

def test_e():
    a = Node(42)

    #      42

    return bottom_right_value(a) # -> 42

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())