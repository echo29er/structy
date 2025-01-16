from typing import Union

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_node_value (head: Node, index: int) -> Union[str, int]:
    """
    Function Purpose: 
        Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

        If there is no node at the given index, then return None.

    Args:
        head (str): the head of a linked list
        index (int): the index of the linked list to get the value from.

    Returns:
        str, int - the value at the index element in the linked list. 

    Assumptions: 
        N/A

    Time complexity: 
        O(n) we traverse each element in the list to find the indexed node. 

    Space complexity: 
        O(n) as we store all elements in the linked list. 
    """

    ###
    # Approach
    ##--------
    # Each element in a linked contains a pointer to the next element. We need a counter starting at 0 to act as the index. We traverse the linked list in O(n), and increment the counter with each traversal.

    counter = 0

    while head is not None:
        if index == counter: 
            return head.val
        counter += 1
        head = head.next
    return None

def test_a():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return get_node_value(a, 2) # 'c'

def test_b():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return get_node_value(a, 3) # 'd'

def test_c():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return get_node_value(a, 7) # None

def test_d():
    node1 = Node("banana")
    node2 = Node("mango")

    node1.next = node2

    # banana -> mango

    return get_node_value(node1, 0) # 'banana'


def test_e():
    node1 = Node("banana")
    node2 = Node("mango")

    node1.next = node2

    # banana -> mango

    return get_node_value(node1, 1) # 'mango'


print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())