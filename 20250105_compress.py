def compress(s: str) -> str:
    """
    Function Purpose: 
        Take a string as an argument, and return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

        Examples            
            'aaa' compresses to '3a'
            'cc' compresses to '2c'
            't' should remain as 't' 

    Args:
        s (string): string of character and integers

    Returns:
        String

    Assumptions: 
        The input only contains alphabetic characters.
        The input is one or more characters.

    Time complexity: 
        O(n) Where n is the length of the string

    Space complexity: 
        O(n) Where n is the length of the string

    """

    # As Python treats everything as a sequence, we can loop through the string.

    # We need to compare each character with the next character to understand the frequency of consecutive characters     

    # Handle first letter and ready previous letter for comparison
        
    def add_sequence(counter, letter):
        if counter == 1:
            return letter
        return str(counter) + letter
    
    previous_letter = s[0]
    counter = 1
    result = ""

    for index in range(1,len(s)): 
        if s[index] == previous_letter:
            counter += 1
        else:
            result += add_sequence(counter, previous_letter)
            counter = 1
        previous_letter = s[index]
    
    # Add last consecutive pattern
    result += add_sequence(counter, previous_letter)
    return result
    
test1 = "a"
test2 = "abc"
test3 = "aaaa"
test4 = "aabcc"

print(compress(test1))
print(compress(test2)) 
print(compress(test3)) 
print(compress(test4))