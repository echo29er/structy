from typing import Union

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

def insert_node (head: Node, value: Union[str, int], target_index: int) -> Node:
    """
    Function Purpose: 
        Write a function, insert_node, that takes in the head of a linked list, a value, and an index. 
        The function should insert a new node with the value into the list at the specified index. 
        The function should return the head of the resulting linked list.

    Args:
        head (Node): the head of a linked list
        target_val (str, int): the target value

    Returns:
        Node: The head of the resulting linked list

    Assumptions: 
        * Consider the head of the linked list as index 0. 
        * Do this in-place.
        * You may assume that the input list is non-empty.
        * You may assume the index is not greater than the length of the input list.

    Time complexity: 
        O(n) we may have to check every element in the list in order to find the node to delete. 

    Space complexity: 
        O(1) because we're only using a constant amount of extra space (the sentinel node and two pointers).
        We are actually modifying the list in-place.
    """

    # For this problem we will need to traverse the linked list until we find the relevant index.
    # When we locate the index we need to insert a new node.
    # We need to point the previous node's .next to the new node, and new node's .next to  

    # Create the new node we'll be inserting 
    new_node = Node(value) 

    # Use a sentinel node to handle insertion at the beginning uniformly 
    sentinel_node = Node(None) # Introduce sentinel aka dummy node. 
    sentinel_node.next = head # Ensure we connect the sentinel node to the existing list
    
    # Set up our pointers
    previous = sentinel_node # We want to print from the sentinel_node.next hence create a separate object to capture the previous node
    current = head # Assign the head to a separate object to act as a pointer
    
    # Move pointers unitl we reach the insertion point 
    # We only need to move to just before the index insertion point
    for index in range(target_index):
        previous = previous.next
        current = current.next

    # Now previous points to the node before our insertion point 
    # and current points to where out new node should point to
    previous.next = new_node
    new_node.next = current

    return sentinel_node.next


def test_a():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return insert_node(a, 'x', 2)
    # a -> b -> x -> c -> d

def test_b():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return insert_node(a, 'v', 3)
    # a -> b -> c -> v -> d

def test_c():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return insert_node(a, 'm', 4)
    # a -> b -> c -> d -> m

def test_d():
    a = Node("a")
    b = Node("b")

    a.next = b

    # a -> b

    return insert_node(a, 'z', 0)
    # z -> a -> b

print(test_a())
print(test_b())
print(test_c())
print(test_d())