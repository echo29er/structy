def pair_product(numbers: list, target_product: int) -> tuple:
    """
    Function Purpose: Take a list and a target product as arguments. The function returns a tuple containing a pair of indices whose elements mulitply to the given target.

    The indices returned must be a unique. One pair is guaranteed to multiply to the target

    Args:
        numbers (list): List of integers
        target_sum (int): Integer that two of the integers in numbers multiply to make

    Returns:
        Tuple

    Time complexity: 
        This is O(n): We go through two loops and searching on a map is O(1)

    Space complexity: 
        This is O(n): we have one map that holds the integers.
    """

    # We can leverage the logic from the pairsum function 

    # Initialise map
    map_of_quotient_to_indices = {}

    # Length of list 
    length_numbers = len(numbers)

    # Populate the map with delta as the key and index as the value
    for index in range(0,length_numbers): 
        quotient = target_product / numbers[index]
        map_of_quotient_to_indices[quotient] = index

    for index, element in enumerate(numbers):
        if element in map_of_quotient_to_indices and index != map_of_quotient_to_indices[element]:
            return index, map_of_quotient_to_indices[element]

print(pair_product([4, 7, 9, 2, 5, 1], 5))