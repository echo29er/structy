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

def create_linked_list (values: list) -> Node:
    """
    Function Purpose: 
        Write a function, create_linked_list, that takes in a list of values as an argument. 
        The function should create a linked list containing each item of the list as the values of the nodes. 
        The function should return the head of the linked list.

    Args:
        values (list): a linked list of values to create a linked list from.

    Returns:
        Node: The head of the resulting linked list

    Assumptions: 
        * N/A

    Time complexity: 
        O(n) as we need to insert at the end of the linked list.

    Space complexity: 
        O(1) to create a linked list. 
    """

    # We want to create a linked list with insertion at the beginning O(1), and then insertion at end O(N)

    # Start the linked list with a sentinel so that we can point from it.
    sentinel_node = Node(None) # Introduce sentinel aka dummy node. 
    start_node = sentinel_node # Create a separate pointer so that we can return from sentinel_node.next at the end.

    for value in values:
        # Generate each node from the list.
        new_node = Node(value)
        start_node.next = new_node # point the start node to the new node.
        start_node = new_node # update the start node to the current node. 
        
    return sentinel_node.next

def test_a():
    return create_linked_list(["h", "e", "y"])
# h -> e -> y

def test_b():
    return create_linked_list([1, 7, 1, 8])
    # 1 -> 7 -> 1 -> 8

def test_c():
    return create_linked_list(["a"])
# a

def test_d():
    return create_linked_list([])
# null


print(test_a())
print(test_b())
print(test_c())
print(test_d())