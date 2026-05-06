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

    # base case no values
    if head is None: 
        return 
    
    # print current value
    print(head.val)
    print_list(head.next)

print_list(a)
    