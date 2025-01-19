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

def merge_lists (head_1: Node, head_2: Node) -> Node:
    """
    Function Purpose: 
        Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. 
        
        The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

        Do this in-place, by mutating the original Nodes.

    Args:
        head_1 (Node): the head of a linked list
        head_2 (Node): the head of a linked list

    Returns:
        Node i.e. the head of the merged linked list

    Assumptions: 
        - Both input lists are non-empty
        - Both lists contain increasing sorted numbers (no duplicates in individual lists)

    Time complexity: 
        O(min(n,m)) as we are evaluating the minimum number of nodes in a list; when we hit the end of a list, we add the remainder to the end of the list we're working with. As there is no sorting then we do not have additional complexity. 

    Space complexity: 
        O(1) we do introduce a new node as a sentinel but that is empty, and insertion is O(1). Other than that we are changing the list in place. 
    """

    # As we know that both input lists contain increasing sorted numbers, we can compare each value in the list in a consecutive way i.e. we do not need to use a sorting algorithm. 
    # We can use a sentinel or dummy node to start the list, and build from it. We can then return its next value at the end. 
    # We point tail equal to sentinel as we need to traverse the list with tail as it is the pointer of the end of the list, but we need to also retain sentinel at the head of the list so we can return the .next value at the end. 
    # To the tail we then keep adding the list_pointer value which is smallest next, and traversing tail. 
    # We can determine which list we've pointed a node to, so we can then traverse that list further. 
    # If there are no further nodes in a list then we simply assign tail.next to the pointer with nodes. 

    first_list_pointer = head_1
    second_list_pointer = head_2
    sentinel = Node(None)
    tail = sentinel

    while first_list_pointer is not None and second_list_pointer is not None:
        
        # Determine which node to start with, using guess and check: 
        node_with_smallest_value = first_list_pointer
        # Using <= ensures stability when duplicate values exist across lists
        if second_list_pointer.val <= first_list_pointer.val: 
            node_with_smallest_value = second_list_pointer
       
        tail.next = node_with_smallest_value
        tail = tail.next

        if node_with_smallest_value == first_list_pointer:
            first_list_pointer = first_list_pointer.next
        else: 
            second_list_pointer = second_list_pointer.next

    if first_list_pointer is not None: # List 2 was exhausted, attach remainder of list 1
        tail.next = first_list_pointer 
    if second_list_pointer is not None: # List 1 was exhausted, attach remainder of list 2
        tail.next = second_list_pointer 

    return sentinel.next

def test_a():
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    q.next = r
    r.next = s
    s.next = t
    # 6 -> 8 -> 9 -> 25

    return merge_lists(a, q)
    # 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 

def test_b():
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(1)
    r = Node(8)
    s = Node(9)
    t = Node(10)
    q.next = r
    r.next = s
    s.next = t
    # 1 -> 8 -> 9 -> 10

    return merge_lists(a, q)
    # 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28 

def test_c():
    h = Node(30)
    # 30

    p = Node(15)
    q = Node(67)
    p.next = q
    # 15 -> 67

    return merge_lists(h, p)
    # 15 -> 30 -> 67


print(test_a())
print(test_b())
print(test_c())