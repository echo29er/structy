class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_values (head: Node) -> list:
    """
    Function Purpose: 
        Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

    Args:
        head (Node): the head of a linked list 

    Returns:
        A list 

    Assumptions: 
        N/A

    Time complexity: 
        O(n) we add each element as we traverse the list.

    Space complexity: 
        O(n) as there are elements that we store. 
    """

    ###
    # Approach
    ##--------
    # Each element in a linked contains a pointer to the next element; therefore we can only traverse a linked list in O(N); we can add an element at head in O(1). We can search and delete in O(N)
    
    new_list = []

    while head is not None:
        new_list.append(head.val)
        head = head.next
    return new_list

def test_a():
    # First test case
    # Instanitate node objects and assign their value
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    # Assign the next attribute a value
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    return linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]

def test_b():
    x = Node("x")
    y = Node("y")

    x.next = y

    # x -> y

    return linked_list_values(x) # -> [ 'x', 'y' ]

def test_c():
    q = Node("q")

    # q

    return linked_list_values(q) # -> [ 'q' ]

def test_d():
    return linked_list_values(None) # -> [ ]


print(test_a())
print(test_b())
print(test_c())
print(test_d())