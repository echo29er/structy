def most_frequent_char(s: str) -> str:
    """
    Function Purpose: Take a string and return the most frequent character. Return the character that appears earlier in the string.
    Assume input string is non-empty.

    Args:
        s (str): String to analyse.

    Returns:
        String

    Time complexity: 
        This is O(n): we have two for loops. 

    Space complexity: 
        This is O(n): we have one map that holds the string.
    """

    # As Python treats all objects as sequences, we can string as sequence of characters. 
    # We can construct a key value map, where the key is the character and the value is the frequency that character is written in the string. 

    # Initialise map
    map_of_characters = {}

    # Enter key values, starting with an empty map
    for character in s: 
        if character not in map_of_characters:
            map_of_characters[character] = 1
        else:
            map_of_characters[character] += 1

    # Here we have a complete key value map, which has taken O(n) to complete.
    # We have to now determine the character with the highest frequency that appears earlier in the string. 
    # We can use the guess and check logic to compare the frequencies. 
    # Since the map is populated based on the order of the for loop, we will guess that the key first key has the highest frequencies and only change guess if the subsequent key has a higher frequency. 

    # Guess: the first key is the result
    most_frequent_character = s[0]

    # Check: against each subsequent key:value pair
    for character in s:
        if map_of_characters[character] > map_of_characters[most_frequent_character]:
            most_frequent_character = character
    return most_frequent_character

print(most_frequent_char("satsuma"))