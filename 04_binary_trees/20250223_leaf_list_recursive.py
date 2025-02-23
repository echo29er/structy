from typing import Union

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leaf_list (root: Node) -> list[list[Union[int, str]]]:
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
        O(n^2) when n is the number of nodes in the tree: 
        - For each node, a new pathj is created by copying and prepending
        - Path copying [root.val] + child_path takes O(h) where h is the height of the tree
        - Balanced tree: paths are length O(log n), but worst case (skewed tree) it's O(n)
        - We do copying for each path that reaches each node
        - Worst case (skewed tree), this leads to O(n^2) 

    Space Complexity: 
        O(n²) in worst case:
        - Each recursive call creates new lists rather than modifying in place
        - For a skewed tree, at the bottom of recursion we're creating paths of length O(n)
        - And we have O(n) such paths being created and copied up the recursion stack
        - The recursion stack itself is O(n) in worst case
        - This leads to O(n²) space usage
    """

    ## RECURSIVE
    # BASE CASES 
    # B1 Empty tree
    # B2 At a leaf 
    
    # B1 Empty tree
    if not root: # same as "if root is None:" 
        return []

    # B2 At a leaf: add value to the array
    if not root.left and not root.right: 
        return[root.val]

    # recursively collect leaf nodes from the left and right subtrees
    left_leaves = leaf_list(root.left)
    right_leaves = leaf_list(root.right)

    # Combine the results 
    return left_leaves + right_leaves


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