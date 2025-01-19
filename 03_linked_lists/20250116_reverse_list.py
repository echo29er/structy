class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list (head: Node) -> Node:
    """
    Function Purpose: 
        Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

    Args:
        head (Node): the head of a linked list

    Returns:
        Node

    Assumptions: 
        N/A

    Time complexity: 
        O(n) to traverse the list and make the changes. 

    Space complexity: 
        O(n) as we hold n elements in the list. 
    """

    ###
    # Approach
    ##--------
    # We are reversing the order in-place. There's something 

    previous_node = None

    while head is not None:
        next_node = head.next
        head.next = previous_node
        previous_node = head
        head = next_node
    return previous_node

def test_a():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # a -> b -> c -> d -> e -> f

    return reverse_list(a) # f -> e -> d -> c -> b -> a

def test_b():
    x = Node("x")
    y = Node("y")

    x.next = y

    # x -> y

    return reverse_list(x) # y -> x


def test_c():
    p = Node("p")

    # p

    return reverse_list(p) # p

print(test_a())
print(test_b())
print(test_c())