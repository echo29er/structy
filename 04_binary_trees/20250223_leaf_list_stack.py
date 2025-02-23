from typing import Union

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leaf_list (root: Node) -> list[Union[int, str]]:
    """
    Function Purpose: 
        Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

    Parameters:
        root (Node): the root of the binary tree.

    Returns:
        list[Union[int, str]]: a list containing the values of all leaf nodes in left-to-right order
        
    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - You may assume that the input tree is non-empty

    Time complexity: 
        O(n) where n is the number of nodes in the tree. We must visit each node in order to generate
        a complete set of branches. 

    Space Complexity: 
        O(h) where n is the number of nodes: 
        - O(h) for the stack during traversal 

    """

    ## ITERATIVE APPROACH USING STACK DUE TO DEPTH FIRST TRAVERSAL
    # Unlike graph traversal, we don't need to track visited nodes as there are no cycles in a tree.

    # As we want to know root to leaf paths, we will use depth first traversal. 
    # We need to:
    # A) work with an empty tree
    # B) understand when we have reached a leaf. 
    # C) as we are dealing with lists, we need to consider an efficient data structure i.e. hmw avoid lists within lists during processing. 

    # DEPTH FIRST TRAVERSAL 
    # As we are working depth first, we are working with a stack that traverse the tree right to left so that we are working in 
    # LiFo.

    # DICTIONARY DATA STRUCTURE
    # In order to track the relations between nodes, we could store this as a list in a tuple in the stack.
    # However this would give us a O(h^2) space complexity as each element in the stack would contain
    # a path list of up to length h.
    # Alternatively, we can populate a dictionary to track the parent-child relationships between the nodes
    # and reconstruct the relationships when we hit a leaf. 
    
    # Empty tree
    if root is None: 
        return []

    # Instantiate and initialise the stack, and instantiate result list
    stack = [root]
    result = []

    # While we have elements to process: 
    while stack: 
        current_node = stack.pop()

        # When we have reached a leaf node, we add the value ot the result list
        if current_node.left is None and current_node.right is None: 
            result.append(current_node.val)

        # Add children to the stack right to left to maintain LiFo
        if current_node.right is not None: 
            stack.append(current_node.right)

        if current_node.left is not None: 
            stack.append(current_node.left)

    return result

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

    return leaf_list(a) # -> [ 'd', 'e', 'f' ] 


def test_b():
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

    return leaf_list(a) # -> [ 'd', 'g', 'h' ]


def test_c():
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

    return leaf_list(a) # -> [ 20, 1, 3, 54 ]


def test_d():
    x = Node('x')

    #      x

    return leaf_list(x) # -> [ 'x' ]



def test_e():
    return leaf_list(None) # -> [ ]



print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())