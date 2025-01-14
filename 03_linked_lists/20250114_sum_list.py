class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sum_list (head: Node) -> list:
    """
    Function Purpose: 
        Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

    Args:
        head (str): the head of a linked list 

    Returns:
        Int

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
    
    summed_value = 0

    while head is not None:
        summed_value += head.val
        head = head.next
    return summed_value

def test_a():
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(-1)
    e = Node(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # 2 -> 8 -> 3 -> -1 -> 7

    return sum_list(a) # 19

def test_b():
    x = Node(38)
    y = Node(4)

    x.next = y

    # 38 -> 4

    return sum_list(x) # 42

def test_c():
    z = Node(100)

    # 100

    return sum_list(z) # 100

def test_d():
    return sum_list(None) # 0

print(test_a())
print(test_b())
print(test_c())
print(test_d())