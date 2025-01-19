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

        You may assume that both input lists are non-empty.

    Args:
        head_1 (Node): the head of a linked list
        head_2 (Node): the head of a linked list

    Returns:
        Node i.e. the head of the merged linked list

    Assumptions: 
        N/A

    Time complexity: 
        O(

    Space complexity: 
        O(
    """



    # Keep track of the end of the tail, the next node and the 
    tail = head_1
    current_1 = head_1.next # start at the second node of list1
    current_2 = head_2 # start at the first node of list2

    while current_1 is not None and current_2 is not None:
        
        # example with head_1 = A -> B -> C -> D and head_2 = 1 -> 2 -> 3 -> 4

        # Store original node of each node's next node
        original_head_1_next = head_1.next # B | C | D
        original_head_2_next = head_2.next # 2 | 3 | 4

        # Zip the nodes i.e. join them 
        head_1.next = head_2 # A -> 1 | B -> 2 | C -> 3
        head_2.next = original_head_1_next # 1 -> B | 2 -> C | C -> 4

        # Move the tail to the last node we attached
        tail = head_2

        # Move the nodes
        head_1 = head_2.next # Move to B | Move to C
        head_2 = original_head_2_next # Move to 2 | Move to 3

    if head_1 is not None: # i.e. head_1 still has nodes
        tail.next = head_1 # point head_2 to the current head_1 
    if head_2 is not None: # i.e. head_2 sitll has nodes
        tail.next = head_2 # point head_1 to the current head_2 


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

print(test_a())
print(test_b())
print(test_c())

