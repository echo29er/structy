def uncompress(s: str) -> str:
    """
    Function Purpose: Take a string as an argument and where it contains an integer before a character return that many copies of the character i.e. 1b2a = baa

    Args:
        s (string): string of character and integers

    Returns:
        String

    Time complexity: 
        O(n * m) as we have to go through all of the elements of the string and these are multiplied by the integers found

    Space complexity: 
        O(n * m) as we hold all elements of the string multipled by the size of the integer

    """

    # As Python treats everything as a sequence, we can loop through the string.
    # We need to ensure that we concatenate and don't add the integer elements of the string. 

    resulting_word = ""
    temp_number = ""

    for element in s: 
        if element.isdigit():
            temp_number += element
        else:
            resulting_word += element * int(temp_number)
            temp_number = ""
    return resulting_word

print(uncompress("3n12e2z")) 
