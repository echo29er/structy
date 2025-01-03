def anagrams(s1: str, s2: str) -> bool: 
    """
    Function Purpose: Compare two strings and return True if they are anagrams i.e. the contain the same characters at the same frequencies.

    Args:
        s1 (str): First string to compare.
        s1 (str): Second string to compare.

    Returns:
        Boolean

    Time complexity: 
        This is O(n + m): we have three for loops. This is faster than comparing using a loop inside a loop which would be a O(n)^2

    Space complexity: 
        This is O(n + m): we have two maps that hold both strings. 
    """
    
    # Base case: If the strings are not the same length then they are not anagrams - return False here immediately completes the function
    if len(s1) != len(s2):
        return False

    # Initialise two maps to hold the characters as keys and the frequency of characters as values
    map_of_letters_s1 = {}
    map_of_letters_s2 = {}

    # Using predicate function, short circuit logic and guess and check logic, set isAnagram to True 
    isAnagram = True 

    # Add key value pairs to the maps
    for letter in s1: 
        if letter not in map_of_letters_s1:
            map_of_letters_s1[letter] = 1
        else: 
            map_of_letters_s1[letter] += 1

    for letter in s2: 
        if letter not in map_of_letters_s2:
            map_of_letters_s2[letter] = 1
        else: 
            map_of_letters_s2[letter] += 1

    # Compare each value in each map. We need to ensure that all keys are check therefore we take the map with the largest amount of values and compare the other map's value to it. 
    # On reflection this is unnecessary as we know the strings are the same length therefore we only need to cycle through the maps once.

    for character in map_of_letters_s1:
        if map_of_letters_s1[character] != map_of_letters_s2.get(character,0):
            return False # Immediately sets the function to false on first valid comparison
    return isAnagram

print(anagrams("potato", "otatop"))