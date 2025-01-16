from typing import Union

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_find (head: Node, target: Union[str, int]) -> bool:
    """
    Function Purpose: 
        Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

    Args:
        head (str): the head of a linked list
        target (str) or (int): a target value to find in the linked list

    Returns:
        bool

    Assumptions: 
        N/A

    Time complexity: 
        O(n) we traverse each element in the list to find the node. 

    Space complexity: 
        O(n) as we store all elements in the linked list. 
    """

    ###
    # Approach
    ##--------
    # Each element in a linked contains a pointer to the next element; therefore we traverse all elements of list until we hit the node with the value, at that point we stop by returning true. 
    # If we traverse all values then no nodes contain the value and we return False. 

    while head is not None:
        if head.val == target:
            return True
        head = head.next
    return False

def test_a():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return linked_list_find(a, "c") # True

def test_b():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return linked_list_find(a, "d") # True

def test_c():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return linked_list_find(a, "q") # False

def test_d():
    node1 = Node("jason")
    node2 = Node("leneli")

    node1.next = node2

    # jason -> leneli

    return linked_list_find(node1, "jason") # True

def test_e():
    node1 = Node(42)

    # 42

    return linked_list_find(node1, 42) # True

def test_f():
    node1 = Node(42)

    # 42

    return linked_list_find(node1, 100) # False


print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
print(test_f())