class Node: 
    def __init__(self, val):
        self.val = val 
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> None

# Traversal algorithm
def print_list(head):
    
    complete_list = []

    while head is not None:
        current_value = head.val 
        print(current_value)
        head = head.next


print_list(a)
    