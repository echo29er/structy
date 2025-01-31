class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        # Convert the linked list to a string representation
        current = self
        values = []
        while current is not None:
            values.append(str(current.val))
            current = current.next
        return ' -> '.join(values)

def add_lists (head_1: Node, head_2: Node) -> Node:
    """
    Function Purpose: 
        Write a function, add_lists, that takes in the head of two linked lists, each representing a number. 
        The nodes of the linked lists contain digits as values. 
        The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. 
        The function should return the head of a new linked listed representing the sum of the input lists. 
        The output list should have its digits reversed as well.

    Args:
        head_1 (Node): a linked list of integers.
        head_2 (Node): a linked list of integers.

    Returns:
        Node: The head of the resulting linked list

    Assumptions: 
        * You must do this by traversing through the linked lists once.

    Time complexity: 
        O(n) as we need to evaluate each node in the linked lists and sum them.

    Space complexity: 
        O(1) to create a new linked list. 
    """

    # We start a new linked list with a sentinel node, which we can then add new nodes to. 
    # We set a moving_node i.e. a pointer to the sentinel. 

    # Start the linked list with a sentinel so that we can point from it.
    sentinel_node = Node(None) # Introduce sentinel aka dummy node. 
    moving_node = sentinel_node # Create a separate pointer so that we can return from sentinel_node.next at the end.
    remainder = 0

    # Helper function 
    def process_node (value, moving_node, remainder):
        # Steps 1 and 2: Calculate the value of the node and handle the remainder
        new_value = value + remainder
        if new_value > 9:
            remainder = 1
            new_value -= 10
        else: 
            remainder = 0

        # Step 3: Create and link new node
        new_node = Node(new_value)
        moving_node.next = new_node
        moving_node = moving_node.next # move to the next node
        
        return moving_node, remainder

    # Process nodes when we have both lists
    while head_1 is not None and head_2 is not None: 
        moving_node, remainder = process_node(head_1.val + head_2.val, moving_node, remainder)
        head_1 = head_1.next
        head_2 = head_2.next
    
    # Process nodes from either list 
    while head_1 is not None: 
        moving_node, remainder = process_node(head_1.val, moving_node, remainder)
        head_1 = head_1.next

    while head_2 is not None: 
        moving_node, remainder = process_node(head_2.val, moving_node, remainder)
        head_2 = head_2.next

    # Handle a final remainder
    if remainder == 1: 
        moving_node.next = Node(remainder)
    
    return sentinel_node.next


def test_a():
    #   621
    # + 354
    # -----
    #   975

    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(6)
    a1.next = a2
    a2.next = a3
    # 1 -> 2 -> 6

    b1 = Node(4)
    b2 = Node(5)
    b3 = Node(3)
    b1.next = b2
    b2.next = b3
    # 4 -> 5 -> 3

    return add_lists(a1, b1)
    # 5 -> 7 -> 9

def test_b():
    #  7541
    # +  32
    # -----
    #  7573

    a1 = Node(1)
    a2 = Node(4)
    a3 = Node(5)
    a4 = Node(7)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    # 1 -> 4 -> 5 -> 7

    b1 = Node(2)
    b2 = Node(3)
    b1.next = b2
    # 2 -> 3 

    return add_lists(a1, b1)
    # 3 -> 7 -> 5 -> 7

def test_c():
    #   39
    # + 47
    # ----
    #   86

    a1 = Node(9)
    a2 = Node(3)
    a1.next = a2
    # 9 -> 3

    b1 = Node(7)
    b2 = Node(4)
    b1.next = b2
    # 7 -> 4

    return add_lists(a1, b1)
    # 6 -> 8    

def test_d():
    #   89
    # + 47
    # ----
    #  136

    a1 = Node(9)
    a2 = Node(8)
    a1.next = a2
    # 9 -> 8

    b1 = Node(7)
    b2 = Node(4)
    b1.next = b2
    # 7 -> 4

    return add_lists(a1, b1)
    # 6 -> 3 -> 1   

def test_e():
    #   999
    #  +  6
    #  ----
    #  1005

    a1 = Node(9)
    a2 = Node(9)
    a3 = Node(9)
    a1.next = a2
    a2.next = a3
    # 9 -> 9 -> 9

    b1 = Node(6)
    # 6

    return add_lists(a1, b1)
    # 5 -> 0 -> 0 -> 1

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())