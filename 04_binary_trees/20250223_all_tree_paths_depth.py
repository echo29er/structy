from typing import Union

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def all_tree_paths (root: Node) -> list[list[Union[int, str]]]:
    """
    Function Purpose: 
        Write a function, all_tree_paths, that takes in the root of a binary tree. 
        The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.
        
        The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

    Parameters:
        root (Node): the root of the binary tree.

    Returns:
        list[list[Union[int, str]]]: a 2d array where each inner array is a root to leaf branch and the outer array is the collection of branches.
        
    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)
        - You may assume that the input tree is non-empty

    Time complexity: 
        O(n) where n is the number of nodes in the tree. We must visit each node in order to generate
        a complete set of branches. 

    Space Complexity: 
        O(n) where n is the number of nodes: 
        - O(h) for the stack during traversal
        - O(n) for the dictionary storing parent-child relationships
        - O(h) for the 2d array as we construct each inner list at only when we hit a leaf. 
        - The dictionary's O(n) space requirement dominates the other terms. 

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

    # Instantiate and initialise the stack, and instantiate the 2d list
    stack = [root]
    paths = []
    
    # Instantiate and initialise a dictionary to track the parent-child relations between nodes
    # If we use a dictionary, this is more efficient than 
    parent_map = {root.val: None} # node_value: parent_value

    # While we have elements to process: 
    while stack: 
        current_node = stack.pop()

        # When we have reached a leaf node, we add the root to leaf path to the 2d list
        if current_node.left is None and current_node.right is None: 
            current_path = [] # Instantiates a new list to add the values/nodes to
            current_value = current_node.val  # Use the values to use the dictionary
            while current_value is not None: 
                current_path.append(current_value)
                current_value = parent_map[current_value] # traverse the parent-child relationship

            current_path.reverse() # reverse the list in place
            paths.append(current_path)

        # Add children to the stack right to left to maintain LiFo
        # Add the relationship of the child to the parent to the dictionary
        if current_node.right is not None: 
            stack.append(current_node.right)
            parent_map[current_node.right.val] = current_node.val

        if current_node.left is not None: 
            stack.append(current_node.left)
            parent_map[current_node.left.val] = current_node.val

    return paths

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

    return all_tree_paths(a) # ->
    # [ 
    #   [ 'a', 'b', 'd' ], 
    #   [ 'a', 'b', 'e' ], 
    #   [ 'a', 'c', 'f' ] 
    # ] 

def test_b():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #         a
    #      /    \
    #     b      c
    #   /  \      \
    #  d    e      f
    #      / \    /   
    #     g  h   i 

    return all_tree_paths(a) # ->
    # [ 
    #   [ 'a', 'b', 'd' ], 
    #   [ 'a', 'b', 'e', 'g' ], 
    #   [ 'a', 'b', 'e', 'h' ], 
    #   [ 'a', 'c', 'f', 'i' ] 
    # ] 

def test_c():
    q = Node('q')
    r = Node('r')
    s = Node('s')
    t = Node('t')
    u = Node('u')
    v = Node('v')

    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v

    #      q
    #    /   \ 
    #   r     s
    #    \
    #     t
    #    /
    #   u
    #  /
    # v

    return all_tree_paths(q) # ->
    # [ 
    #   [ 'q', 'r', 't', 'u', 'v' ], 
    #   [ 'q', 's' ] 
    # ] 


def test_d():
    z = Node('z')

    #      z

    return all_tree_paths(z) # -> 
    # [
    #   ['z']
    # ]

print(test_a())
print(test_b())
print(test_c())
print(test_d())