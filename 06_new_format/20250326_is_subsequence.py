def is_subsequence(sub_string, string_tester):
    """
    Function purpose: 
        Write a function, is_subsequence, that takes in sub_string and string_tester. 
        The function should return a boolean indicating whether or not sub_string is a subsequence of string_tester.

        A subsequence is a string that can be formed by deleting 0 or more characters from another string.

    Parameters: 
        sub_string (str): string that contains that sub string
        string_tester (str): string in which we want to see if sub_string exists

    Returns: 
        bool: True if string_tester contains sub_string, and False if it does not.

    Assumptions: 
        * We don't need to handle empty parameters
        * We don't need to handle incorrect data types

    Complexity: 
        Time Complexity: O(N) where N is the length of string_tester. In the worst case, you'll need to traverse the entire string_tester once.
        Space Complexity: O(1) (constant), not O(N). Your algorithm only uses a fixed number of variables (pointer_a, pointer_b, comparison, length_sub_string) regardless of the input size. You're not creating any data structures that grow with the input size.
    """

    """
    Scratchpad
    * The sub_string "abd" must return True when the string_tester is "abcd"; therefore we need to evaluate each letter
    * We can therefore use a two-pointer approach for this.
    """

    # Instantiations
    length_sub_string = len(sub_string)
    comparison = 0
    pointer_a = pointer_b = 0

    while pointer_a < len(sub_string) and pointer_b < len(string_tester):
        if sub_string[pointer_a] == string_tester[pointer_b]: 
            pointer_a += 1
            pointer_b += 1
            comparison += 1
        elif sub_string[pointer_a] != string_tester[pointer_b]:
            pointer_b += 1
        
    if length_sub_string == comparison:
        return True
    else: 
        return False