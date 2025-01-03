def pair_sum(numbers: list, target_sum: int) -> tuple:
    """
    Function Purpose: Take a list and a target sum as arguments. The function returns a tuple containing a pair of indices whose elements sum to the given target.

    The indices returned must be a unique. One pair is guaranteed to sum to the target

    Args:
        numbers (list): List of integers
        target_sum (int): Integer that two of the integers in numbers sum to make

    Returns:
        Tuple

    Time complexity: 
        This is O(n): We go through two loops and searching on a map is O(1)

    Space complexity: 
        This is O(n): we have one map that holds the integers.
    """

    # We need to cycle through each integer and understand its addition with every other number.
    # We can achieve this using a for loop on another for loop on the list however this will give us a time complexity of O(n)^2.
    # Alternatively, we can use a map: 
    # As we want to retrieve the indices from the list, these will be the values. The keys will need to be something we can compare to the list's elements.  
    # The keys therefore will be the delta of the subtraction of the target_sum and the each element in the list.
    # We can then perform a for loop on the list to compare it with , and determine if the element matches any of the values in the map. 

    # Initialise map
    map_of_deltas_to_indices = {}

    # Length of list 
    length_numbers = len(numbers)

    # Populate the map with delta as the key and index as the value
    for index in range(0,length_numbers): 
        delta = target_sum - numbers[index]
        map_of_deltas_to_indices[delta] = index

    for index, element in enumerate(numbers):
        if element in map_of_deltas_to_indices and index != map_of_deltas_to_indices[element]:
            return index, map_of_deltas_to_indices[element]


numbers = [ i for i in range(1, 6001) ]
print(pair_sum(numbers, 11999)) # -> (5998, 5999)