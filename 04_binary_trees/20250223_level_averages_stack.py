class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_averages (root: Node) -> list:
    """
    Function Purpose: 
        Write a function, level_averages, that takes in the root of a binary tree that contains number values. 
        The function should return a list containing the average value of each level.
    
    Parameters:
        root (Node): the root of the binary tree.

    Returns:
        list: containing the average value of each level.
        
    Assumptions: 
        - The tree is a valid binary tree (each node has 0-2 children)

    Time complexity: 
        O(n) where n is the number of nodes - each node is processed exactly once during the
        breadth-first traversal.

    Space Complexity: 
        O(w) where w is the maximum width of the tree. This comes from:
        - The queue which holds at most one level's worth of nodes
        - The dictionary storing nodes by level
        - The final result list

    """

    ## ITERATIVE APPROACH USING STACK DUE TO DEPTH FIRST TRAVERSAL
    # This implementation uses an iterative depth-first search (DFS) approach with a stack.
    # While we're getting level ordering, DFS still works because we track each node's level
    # explicitly rather than relying on the traversal order.

    # Trees vs Graphs: An Important Distinction
    # Unlike graph traversal, we don't need to track visited nodes here because trees are
    # acyclic by definition - there's exactly one path from root to any node.

    # Key Implementation Goals:
    # 1. Handle empty trees gracefully
    # 2. Track each node's level while traversing
    # 3. Group nodes efficiently by level without storing redundant information

    # Data Structure Choice:
    # We use two main structures:
    # 1. Stack: For DFS traversal, storing (node, level) pairs
    # 2. Dictionary: Maps levels to sum and to count, allowing O(1) grouping
    
    # Empty tree case - return empty list as there are no levels to process
    if root is None: 
        return []

    # Initialize our core data structures:
    # - Stack starts with root node at level 0
    # - level_sums will group node values by their levels
    # - level_counts
    # - results will hold our final level-ordered lists
    stack = [(root,0)] # root, level
    level_sums = {}
    level_counts = {}
    
    # Process nodes using depth-first traversal 
    while stack: 
        # Pop returns the most recently added node (LIFO - Last In, First Out)
        current_node, level = stack.pop()

        # Ensure we initialise for each level sum and level count
        if level not in level_sums: 
            level_sums[level] = 0
            level_counts[level] = 0

        # For the current node, add its value and count according to its level
        level_sums[level] += current_node.val
        level_counts[level] += 1

        # Add children to stack with their level (parent's level + 1)
        # We add right child first so left child gets processed first (LIFO)
        if current_node.right: 
            stack.append((current_node.right, level+1))
        if current_node.left: 
            stack.append((current_node.left, level+1))

    results = []
    for key in level_sums: 
        results.append(level_sums[key] / level_counts[key])

    return results

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

    return level_averages(a) # -> [ 3, 7.5, 1 ] 

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

    return level_averages(a) # -> [ 5, 32.5, 17.5, 2 ] 

def test_c():
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(45)
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
    # -3   0     45
    #     /       \
    #    -1       -2

    return level_averages(a) # -> [ -1, -5.5, 14, -1.5 ]

def test_d():
    q = Node(13)
    r = Node(4)
    s = Node(2)
    t = Node(9)
    u = Node(2)
    v = Node(42)

    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v

    #        13
    #      /   \
    #     4     2
    #      \
    #       9
    #      /
    #     2
    #    /
    #   42

    return level_averages(q) # -> [ 13, 3, 9, 2, 42 ]

def test_e():
    return level_averages(None) # -> [ ]


print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())