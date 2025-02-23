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
        O(n) where n is the number of nodes in the tree:
        - Each node is visited exactly once
        - Level grouping operations are O(1) using dictionary

    Space Complexity: 
        O(w) where w is the maximum width of the tree:
        - Queue stores at most one level's worth of nodes
        - Dictionary stores node values grouped by level
        - Both are bounded by the tree's maximum width
        - Final result takes O(n) space to store all node values

    """

    ## ITERATIVE APPROACH USING QUEUE DUE TO BREADTH FIRST TRAVERSAL
    # This implementation uses breadth-first search (BFS) to traverse the tree level by level.
    # BFS is particularly well-suited for level-order traversal as it naturally processes 
    # all nodes at the current level before moving to the next level.

    # Trees vs Graphs: A Key Distinction
    # In trees, we don't need to track visited nodes because trees are acyclic by definition.
    # There's exactly one path from the root to any node, so we'll never revisit a node.

    # Implementation Strategy:
    # We use two main data structures to efficiently capture level information:
    # 1. Queue: Processes nodes in FIFO (First In, First Out) order, maintaining level order
    # 2. Dictionary: Groups nodes by their level for easy retrieval and organization

    # Time and Space Efficiency:
    # By using a dictionary to group nodes by level as we traverse, we avoid:
    # - Creating separate lists for each level during traversal
    # - Multiple passes through the tree
    # - Excessive memory usage from duplicating node information
    
    # Empty tree
    if root is None: 
        return []

    # Initialize our data structures:
    # - Queue starts with root node at level 0, using deque for O(1) operations
    # - level_map will group node values by their level
    # - results will store our final ordered list of levels
    queue = [(root,0)] # Using deque for efficient queue operations # Each entry is (node, level) pair
    level_sums = {}
    level_counts = {}
    pointer = 0
    
    # Process nodes level by level
    while pointer < len(queue): 
        # popleft() gives us FIFO behavior - essential for processing levels in order
        current_node, level = queue[pointer]

        # Ensure we initialise for each level sum and level count
        if level not in level_sums: 
            level_sums[level] = 0
            level_counts[level] = 0

        # For the current node, add its value and count according to its level
        level_sums[level] += current_node.val
        level_counts[level] += 1

        # Add children to the queue left to right to maintain FiFo
        if current_node.left: 
            queue.append((current_node.left, level+1))
        if current_node.right: 
            queue.append((current_node.right, level+1))
    
        pointer += 1

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