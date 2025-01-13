def fibonacci(number: int) -> bool:
    """
    Function Purpose: 
        Write a function, fibonacci, that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

        Examples            
            fibonacci(1); # -> 1

    Args:
        number (int): a number 

    Returns:
        Number

    Assumptions: 
        Solve this recursively.

    Time complexity: 
        O(2^n) because each call spawns two more calls: it effectively forms a binary tree of depth n

    Space complexity: 
        O(n) each call stores a small, constant amount of data. 
    """

    ###
    # Approach to fibonacci without recursion
    ##----------------------------------------
    # We add the previous value and the current value to give the next value.
    
    if number <= 1:
        return number
    
    previous = 0
    current = 1
    for index in range(2, number + 1): # we start at 2 because 0 and 1 are base cases
        next = previous + current
        previous = current
        current = next 
    return current 

    ###
    # Approach to fibonacci using recursion
    # -------------------------------------
    # Initial Analysis
    # We know that the fibonacci sequence is the where the current element is the sum of the previous two elements.
    # Therefore we need to find the fibonacci value for the two preceding elements and then sum them. 

    # Base case: 0 or 1 character return the number 
    # if number <= 1: 
    #     return number
    # # Compare from the outer numbers and move in
    # return fibonacci(number-1) + fibonacci(number-2)

# Testing
## Test Cases
test_cases = [0,1,2,3,4,5,8]

# ## Invocation
for number in test_cases: 
    print(fibonacci(number))