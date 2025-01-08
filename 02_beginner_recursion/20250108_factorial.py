def factorial(number: int) -> int:
    """
    Function Purpose: 
        Write a function, factorial, that takes in a number n and returns the factorial of that number. The factorial of n is the product of all the positive numbers less than or equal to n. 

        Examples            
            sum_numbers_recursive([5, 2, 9, 10]); # -> 26

    Args:
        number (int): an integer 

    Returns:
        Integer

    Assumptions: 
        Solve this recursively.
        You can assume that n is a non-negative integer. Note that the factorial of 0 is defined to be 1.

    Time complexity: 
        O(n) as we make n recursive calls.

    Space complexity: 
        O(n) due to the recursive call stack.

    """

    # base case 
    if number == 1 or number == 0:
        return 1
    
    return factorial(number - 1) * number

print(factorial(3))