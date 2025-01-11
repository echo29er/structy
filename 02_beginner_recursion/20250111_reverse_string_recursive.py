def reverse_string(string_a: str) -> str:
    """
    Function Purpose: 
        Write a function, reverse_string, that takes in a string as an argument. The function should return the string with its characters in reverse order.

        Examples            
            reverse_string("hello") # -> "olleh"

    Args:
        string (str): a string 

    Returns:
        String

    Assumptions: 
        Solve this recursively.

    Time complexity: 
        O(n^2) due to string slicing and concatenation

    Space complexity: 
        O(n^2)

    """

    ###
    # Approaches to reverse a string without recursion
    
    ## Using pointers and string concatenation
    ##----------------------------------------
    ## This is memory intensive as a new string is required at each addition to the string reference. Strings are immutable
    # left_pointer = 0
    # right_pointer = len(string_a)-1
    # reversed_string = ""

    # while left_pointer <= right_pointer:
    #     reversed_string += string_a[right_pointer]
    #     right_pointer -= 1
    # return reversed_string
    ###

    ## Coverting to a list, using pointers and swapping elements
    ##----------------------------------------------------------
    ## While this requires conversion to a list it is more memory efficient as lists are mutable. 
    # list_string = list(string_a)
    # left_pointer = 0
    # right_pointer = len(list_string)-1

    # while left_pointer < right_pointer:
    #     list_string[left_pointer], list_string[right_pointer] = list_string[right_pointer],list_string[left_pointer]
    #     left_pointer += 1
    #     right_pointer -= 1
    # return "".join(list_string)
    ###

    ## Pythonic way
    ##-------------
    ## Use the slicing functionality
    # reversed_string = string_a[::-1]
    # return reversed_string
    ###

    ###
    # Approach to reverse a string with recursion
    # -------------------------------------------
    # Initial Analysis
    # Strings are immutable, so we will either need to create a new string or convert to a list. 
    # Let's start by considering how we can break down a string to work recursively and end up with a base case that will allow the stack to unravel. 
    # If we take "abcd", we have "a" + "bc" then we can get "b" + "c". 
    # Our base case is there's one character or less, so we re

    # Base cases are the string is empty and the string has one character i.e. return the first character
    # We return the last character, and then run recursion on the reversed string until we hit the base case. 

    if len(string_a) == 0:
        return ""
    
    if len(string_a) == 1:
        return string_a[0]
    
    return  string_a[len(string_a)-1] + reverse_string(string_a[:-1])

# Testing
## Test Cases
test_cases = ["hello","abcdefg","stopwatch",""]

# ## Invocation
for string in test_cases: 
    print(reverse_string(string))