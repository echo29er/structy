class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_univalue_list (head: Node) -> Node:
    """
    Function Purpose: 
        Write a function, is_univalue_list, that takes in the head of a linked list as an argument. 
        The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

    Args:
        head (Node): the head of a linked list

    Returns:
        Boolean

    Assumptions: 
        You may assume that the input list is non-empty.

    Time complexity: 
        O(n) we may have to check every element in the list; however this could return a False value on the second element so this is the worst case. 

    Space complexity: 
        O(1) as we are not affecting the linked list.
    """

    # For this problem we need to traverse the entire linked list. We can assign the value of the head of the list to a variable: unique_value. 
    # We can use a guess and check pattern by assuming that the outcome is True. We check each node's value against unique_value and if there's no match then return False.

    unique_value = head.val

    # Traverse the list
    while head is not None: 
        if head.val != unique_value:
            return False
        head = head.next
    return True


def test_a():
    a = Node(7)
    b = Node(7)
    c = Node(7)

    a.next = b
    b.next = c

    # 7 -> 7 -> 7

    return is_univalue_list(a) # True

def test_b():
    a = Node(7)
    b = Node(7)
    c = Node(4)

    a.next = b
    b.next = c

    # 7 -> 7 -> 4

    return is_univalue_list(a) # False

def test_c():
    u = Node(2)
    v = Node(2)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 2 -> 2 -> 2 -> 2

    return is_univalue_list(u) # True

def test_d():
    u = Node(2)
    v = Node(2)
    w = Node(3)
    x = Node(3)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 2 -> 3 -> 3 -> 2

    return is_univalue_list(u) # False

def test_e():
    z = Node('z')

    # z

    return is_univalue_list(z) # True

def test_f():
    u = Node(2)
    v = Node(1)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 1 -> 2 -> 2 -> 2

    return is_univalue_list(u) # False

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
print(test_f())