def sum_of_lengths(strings: list) -> int:
    """
    Function Purpose: 
        Write a function sumOfLengths that takes in a list of strings and returns the total length of the strings.

        Examples            
            sum_of_lengths(['goat', 'cat', 'purple']) # -> 13

    Args:
        strings (list): a list of strings 

    Returns:
        Integer

    Assumptions: 
        Solve this recursively.

    Time complexity: 
        O(n^2) recursive call for the recursion then we have to copy the arrays.

    Space complexity: 
        O(n^2) recursive call for the recursion then we have to copy the arrays.

    """

    # We need to shrink the problem size e.g. 
    # sum_of_lengths(['goat', 'cat', 'purple']) -> 13
    # sum_of_lengths(['cat', 'purple']) -> 9
    # sum_of_lengths(['purple']) -> 6
    # sum_of_lengths([]) -> 0 This is the base case

    if len(strings) == 0:
        return 0
    
    return len(strings[0])+ sum_of_lengths(strings[1:]) 

print(sum_of_lengths(['goat','coat'])) # -> 13
