def intersection(list_a: list, list_b: list) -> list:
    """
    Function Purpose: 
        Write a function, intersection, that takes in two lists, list_a, list_b, as arguments. The function should return a new list containing elements that are in both of the two lists.

        Examples            
            intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6] 

    Args:
        list_a (list): a list of integers
        list_b (list): a list of integers

    Returns:
        List

    Assumptions: 
        You may assume that each input list does not contain duplicate elements.

    Time complexity: 
        O(n + m) as we need to iterate through each list 

    Space complexity: 
        O(n + m) where n is list_a and m is list_b

    """

    # We could run a for loop in a for loop to compare each element within one list with another; however we will end up with a time complexity of O(n)^2
    # Therefore we can leverage a map as an alternative data structure:
    # 1. Determine the list with the most elements.
    # 2. Add these elements as keys to a map O(n) as we need to iterate through all values in the list, and set the values for each to 0. 
    # 3. Run a for loop on the other list O(m) to see if the element is a key of the map O(1).
    # 4. If there's a match add that key to a new list O(1).

    # Use guess and check pattern
    largest_list = list_a
    smallest_list = list_b

    if len(list_b) > len(largest_list): 
        largest_list = list_b
        smallest_list = list_a

    # Add list elements to a map
    temp_map = {}
    for element in largest_list: # O(n) where n is length of larger list
        temp_map[element] = 0

    # Search map with smallest list and add values to a results_list
    results_list = []
    for element in smallest_list: # O(m) where m is length of smaller list
        if element in temp_map: # O(1) lookup in map/dictionary
            results_list.append(element)

    return results_list

# Testing
test_case_a = intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6] 
test_case_b = intersection([2,4,6], [4,2]) # -> [2,4]
test_case_c = intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
test_case_d = intersection([0,1,2], [10,11]) # -> []
a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
# test_case_e = intersection(a, b) # -> [0,1,2,3,..., 49999]

print(test_case_a)
print(test_case_b)
print(test_case_c)
print(test_case_d)
# print(test_case_e)