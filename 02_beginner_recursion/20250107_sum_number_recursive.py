def sum_numbers_recursive(numbers: list) -> int:
    """
    Function Purpose: 
        Write a function sumNumbersRecursive that takes in an array of numbers and returns the sum of all the numbers in the array. 

        Examples            
            sum_numbers_recursive([5, 2, 9, 10]); # -> 26

    Args:
        numbers (list): a list of integers

    Returns:
        Integer

    Assumptions: 
        All elements will be integers. Solve this recursively.

    Time complexity: 
        O(n^2) as we make n recursive calls and use sliced subarrays

    Space complexity: 
        O(n^2) due to the recursive call stack and sliced subarrays
    

    """

    # We think about how we can break this problem down into smaller pieces. 
    # The smallest piece is where the list is empty or when it's only got on element.

    # base case list is empty
    if len(numbers) == 0:
        return 0
    
    # base case one number 
    if len(numbers) == 1:
        return numbers[0]

    # Using a loop would be a form of iteration, so we need to think how we can relate the sum of n numbers to the sum of n-1 numbers. We could start at the length of the list and -1 each time. 

    # numbers[:-1] takes all elements except the last one, making the problem smaller each time

    # numbers[len(numbers)-1] takes the last element and adds it to our recursive sum

    return sum_numbers_recursive(numbers[:-1]) + numbers[len(numbers)-1]

test_case_a = sum_numbers_recursive([5, 2, 9, 10]); # -> 26
test_case_b = sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1]); # -> 1
test_case_c = sum_numbers_recursive([]); # -> 0
test_case_d = sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1]); # -> 1001
test_case_e = sum_numbers_recursive([700, 70, 7]); # -> 777
test_case_f = sum_numbers_recursive([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]); # -> -55
test_case_g = sum_numbers_recursive([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]); # -> 0
test_case_h = sum_numbers_recursive([123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0]); # -> 137174205

print(test_case_a)
print(test_case_b)
print(test_case_c)
print(test_case_d)
print(test_case_e)
print(test_case_f)
print(test_case_g)
print(test_case_h)