def palindrome(string: str) -> bool:
    """
    Function Purpose: 
        Write a function, palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards.

        Examples            
            palindrome("pop") # -> True

    Args:
        string (str): a string 

    Returns:
        Boolean

    Assumptions: 
        Solve this recursively.

    Time complexity: 
        O(n^2) Each recursive call takes a slice of the string (string[1:-1]), which is O(n). We do this n/2 times (each time checking outer pairs). So it's actually O(n²) because of the string slicing operation

    Space complexity: 
        O(n) because of the recursive call stack

    """

    ###
    # Approaches to determine a palindrome without recursion
    
    ## Using pointers
    ##----------------------------------------
    # We guess that the string is a palindrome, unless we find that it is not.
    # left_pointer = 0
    # right_pointer = len(string)-1

    # while left_pointer <= right_pointer:
    #     if string[left_pointer] != string[right_pointer]:
    #         return False # Circuit breaker logic
    #     left_pointer += 1
    #     right_pointer -= 1

    # return True
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

    ## Pythonic way (1)
    ##-----------------
    ## Use the string reversal comparsion
    # return string == string[::1] # returns True if correct
    ###

    ## Pythonic way (2)
    ##-----------------
    ## Use the built in reversed()
    # return string == ''.join(reversed(string))
    ###

    ###
    # Approach to reverse a string with recursion
    # -------------------------------------------
    # Initial Analysis
    # We're not mutating a string, we're only checking it.
    # How do we break this into smaller chunks?
    # Let's consider the base cases: 
    # No characters or one character is true. Two characters is the first to be evaluated - if they equal each other then true 
    # If we have "abccba" then we need to compare the outside, and come in.
    # We isolate the first and last elements, and then we call it on the neighours right of the first and left of the last, and we continue doing that until we hit one character.
    # If any outer pair is false then we immediately return false

    # Base case 1: no character or 1 character: True
    if len(string) <= 1: 
        return True
        
    # Compare from the outer numbers and move in
    return string[0] == string[-1] and palindrome(string[1:-1]) # Where string[-1] returns the last character

# Testing
## Test Cases
test_cases = ["pop","kayak","pops","boot","rotator","abcbca",""]

# ## Invocation
for string in test_cases: 
    print(palindrome(string))