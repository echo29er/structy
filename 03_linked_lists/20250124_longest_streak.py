class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def longest_streak (head: Node) -> int:
    """
    Function Purpose: 
        Write a function, longest_streak, that takes in the head of a linked list as an argument. 
        The function should return the length of the longest consecutive streak of the same value within the list.

    Args:
        head (Node): the head of a linked list

    Returns:
        int: the length of the longest consecutive streak of the same value within the list 

    Assumptions: 
        N/A

    Time complexity: 
        O(n) we may have to check every element in the list.

    Space complexity: 
        O(1) as we are not affecting the linked list.
    """

    # For this problem we will need to traverse the whole linked list. 
    # We will need two counters: current_counter that holds the value of the most recent streak, and longest_streak_value the holds the largest streak value.
    # We can start with the guess and check pattern. 

    if head is None: 
        return 0

    # if head is not None then we traverse the list. 
    # We know the first element will give us a streak size of 1, which is therefore the longest streak value 
    recent_streak = longest_streak_value = 1
    while head is not None and head.next is not None: 
        if head.val == head.next.val: 
            recent_streak +=1 
            if recent_streak > longest_streak_value:
                    longest_streak_value = recent_streak
        else: 
            recent_streak = 1
        head = head.next
    return longest_streak_value


def test_a():
    a = Node(5)
    b = Node(5)
    c = Node(7)
    d = Node(7)
    e = Node(7)
    f = Node(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # 5 -> 5 -> 7 -> 7 -> 7 -> 6

    return longest_streak(a) # 3

def test_b():
    a = Node(3)
    b = Node(3)
    c = Node(3)
    d = Node(3)
    e = Node(9)
    f = Node(9)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # 3 -> 3 -> 3 -> 3 -> 9 -> 9

    return longest_streak(a) # 4

def test_c():
    a = Node(9)
    b = Node(9)
    c = Node(1)
    d = Node(9)
    e = Node(9)
    f = Node(9)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # 9 -> 9 -> 1 -> 9 -> 9 -> 9

    return longest_streak(a) # 3

def test_d():
    a = Node(5)
    b = Node(5)

    a.next = b

    # 5 -> 5

    return longest_streak(a) # 2


def test_e():
    a = Node(4)

    # 4

    return longest_streak(a) # 1

def test_f():
    return longest_streak(None) # 0


print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
print(test_f())