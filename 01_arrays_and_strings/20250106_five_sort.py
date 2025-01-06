def five_sort(list_a: list) -> list:
    """
    Function Purpose: 
        Write a function, five_sort, that takes in a list of numbers as an argument. The function should rearrange elements of the list such that all 5s appear at the end. Your function should perform this operation in-place by mutating the original list. The function should return the list.

        Examples            
            five_sort([12, 5, 1, 5, 12, 7]) -> [12, 7, 1, 12, 5, 5] 

    Args:
        list_a (list): Modified original list with all 5s at the end

    Returns:
        list_a i.e. original list

    Assumptions: 
        Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.

    Time complexity: 
        O(n) because each element is only examined once or twice maximum as the pointers move towards each other from opposite ends

    Space complexity: 
        O(1) as swaps are in place. 

    """

    # For this we use a while loop.
    # We start the pointers at opposite ends of the list. While the right pointer is larger than the left pointer, we keep moving the right pointer until we find a non 5, we then look at the left pointer, and if the left == 5 then we swap the values.

    left_pointer = 0 # start at the index on the left most side
    right_pointer = len(list_a)-1 # start at the index on the right most side

    while right_pointer > left_pointer: # Ensure the pointers do not crossover i.e. no numbers left to swap
        if list_a[right_pointer] == 5: # Stops the left pointer from moving  
            right_pointer -= 1
        elif list_a[left_pointer] == 5: 
            list_a[left_pointer], list_a[right_pointer] = list_a[right_pointer], list_a[left_pointer]
            left_pointer += 1
        else: 
            left_pointer += 1
    return list_a

# Testing

test_case_d = five_sort([5, 5, 6, 5, 5, 5, 5]) # -> [6, 5, 5, 5, 5, 5, 5] 
test_case_e = five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]) # -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 
test_case_a = five_sort([12, 5, 1, 5, 12, 7]) # -> [12, 7, 1, 12, 5, 5] 
test_case_b = five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]) # -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
test_case_c = five_sort([5, 5, 5, 1, 1, 1, 4]) # -> [4, 1, 1, 1, 5, 5, 5] 
fours = [4] * 20000
fives = [5] * 20000
nums = fours + fives
# test_case_f = five_sort(nums)
# twenty-thousand 4s followed by twenty-thousand 5s -> [4, 4, 4, 4, ..., 5, 5, 5, 5]

print(test_case_a)
print(test_case_b)
print(test_case_c)
print(test_case_d)
print(test_case_e)
# print(test_case_f)