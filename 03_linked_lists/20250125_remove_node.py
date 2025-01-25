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

def remove_node (head: Node, target_val: Union[str, int]) -> Node:
    """
    Function Purpose: 
        Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. 
        The function should delete the node containing the target value from the linked list and 
        return the head of the resulting linked list. 

    Args:
        head (Node): the head of a linked list
        target_val (str, int): the target value

    Returns:
        Node: The head of the resulting linked list

    Assumptions: 
        * If the target appears multiple times in the linked list, only remove the first instance of the target in the list.
        * Do this in-place.
        * You may assume that the input list is non-empty.
        * You may assume that the input list contains the target.

    Time complexity: 
        O(n) we may have to check every element in the list in order to find the node to delete. 

    Space complexity: 
        O(1) because we're only using a constant amount of extra space (the sentinel node and two pointers).
        We are actually modifying the list in-place.
    """

    # For this problem we will need to traverse the linked list until we find the node to delete.  
    # When we locate the node to delete, we will need to change the .next value of the previous node to point to 
    # the deletion node's .next value.
    # As this is a singly linked list, we can expose the required value using .next.val. That is to say
    # Node("A") -> Node("B") -> Node("C"). Value = "B" is required to be deleted. 
    # So we say if Node("A").next.val == "B" then Node("A").next = Node("A").next.next.
    # Edge cases we need to deal with is:
    # A) when If .next.next doesn't exist: here .next need to be set to None, and 
    # B) when the Node for deletion is at the start of the list: here we can prepend the list with a sentinel. 
    # We can then change the .next 
    # Noting the assumptions we don't deal with empty lists or lists without the value. 

    sentinel_node = Node(None) # Introduce sentinel aka dummy node. 
    previous = sentinel_node # We want to print from the sentinel_node.next hence create a separate object to capture the previous node
    current = head # Assign the head to a separate object to act as a pointer
    sentinel_node.next = current # Ensure we connect the sentinel node to the existing list
    while current is not None: 
        if current.val == target_val: # Check for the target value
            previous.next = current.next # Change the .next pointer of the previous node to the current.next's
            return sentinel_node.next # Return the head of the list dropping the sentinel/dummy as we only drop the first instance of the target value
        else: 
            previous = previous.next # Move previous forward
        current = current.next # Move current forward
    return sentinel_node.next # Return the head of the list dropping the sentinel/dummy node


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

    return remove_node(a, "c")
    # a -> b -> d -> e -> f

def test_b():
    x = Node("x")
    y = Node("y")
    z = Node("z")

    x.next = y
    y.next = z

    # x -> y -> z

    return remove_node(x, "z")
    # x -> y

def test_c():
    q = Node("q")
    r = Node("r")
    s = Node("s")

    q.next = r
    r.next = s

    # q -> r -> s

    return remove_node(q, "q")
    # r -> s

def test_d():
    node1 = Node("h")
    node2 = Node("i")
    node3 = Node("j")
    node4 = Node("i")

    node1.next = node2
    node2.next = node3
    node3.next = node4

    # h -> i -> j -> i

    return remove_node(node1, "i")
    # h -> j -> i

def test_e():
    t = Node("t")

    # t

    return remove_node(t, "t")
    # None

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())