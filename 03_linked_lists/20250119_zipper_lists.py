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

def zipper_lists (head_1: Node, head_2: Node) -> Node:
    """
    Function Purpose: 
        Write a function, zipper_lists, that takes in the head of two linked lists as arguments. 
        
        The function should zipper the two lists together into single linked list by alternating nodes. 
        
        If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. 
        
        The function should return the head of the zippered linked list.

        Do this in-place, by mutating the original Nodes.


    Args:
        head_1 (Node): the head of a linked list
        head_2 (Node): the head of a linked list

    Returns:
        Node i.e. the head of the merged linked list

    Assumptions: 
        Both input lists are non-empty

    Time complexity: 
        O(min(m,n)) our traversal length is equal to the length of the smallest list. When one list is exhausted we simply point to the rest of the remaining contiguous list in O(1)

    Space complexity: 
        O(1) as we are mutating this list in place.
    """


    # Using three pointers: one to track the last node of the list (tail), one to track the position on the first_list, and one to track the position of the second_list. 
    # tail - we keep track of the last node of the list in order to append the remainder of the list when one list becomes empty. 
    # first_list_pointer - we track the current node of the element in the first linked list. 
    # second_list_pointer - we track the current node of the element in the second linked list.

    # 
    tail = head_1
    first_list_pointer = head_1
    second_list_pointer = head_2

    while first_list_pointer is not None and second_list_pointer is not None:
        
        # example with head_1 = A -> B -> C -> D and head_2 = 1 -> 2 -> 3 -> 4

        # Store original node of each node's next node
        first_list_pointer_next = first_list_pointer.next # B | C | D
        second_list_pointer_next = second_list_pointer.next # 2 | 3 | 4

        # Repoint the current nodes to the correct next node
        first_list_pointer.next = second_list_pointer # A -> 1 | B -> 2 | C -> 3
        second_list_pointer.next = first_list_pointer_next # 1 -> B | 2 -> C | C -> 4

        # Move the tail to the last node we attached
        tail = second_list_pointer

        # Move the nodes
        first_list_pointer = second_list_pointer.next # Move to B | Move to C
        second_list_pointer = second_list_pointer_next # Move to 2 | Move to 3

    if first_list_pointer is not None: # List 2 was exhausted, attach remainder of list 1
        tail.next = first_list_pointer 
    if second_list_pointer is not None: # List 1 was exhausted, attach remainder of list 2
        tail.next = second_list_pointer 


    return head_1

def test_a():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    # a -> b -> c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    return zipper_lists(a, x)
    # a -> x -> b -> y -> c -> z

def test_b():
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

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    return zipper_lists(a, x)
    # a -> x -> b -> y -> c -> z -> d -> e -> f

def test_c():
    s = Node("s")
    t = Node("t")
    s.next = t
    # s -> t

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.next = two
    two.next = three
    three.next = four
    # 1 -> 2 -> 3 -> 4

    return zipper_lists(s, one)
    # s -> 1 -> t -> 2 -> 3 -> 4

def test_d():
    w = Node("w")
    # w

    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    # 1 -> 2 -> 3 

    return zipper_lists(w, one)
    # w -> 1 -> 2 -> 3

def test_e():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    # 1 -> 2 -> 3 

    w = Node("w")
    # w

    return zipper_lists(one, w)
    # 1 -> w -> 2 -> 3

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())