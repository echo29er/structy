from typing import List
from utilities.test_runner import test_runner

"""
Function purpose: 
Write a function, all_even, that takes in a list of numbers as an argument. The function should return a boolean indicating whether or not every element of the list is an even number.

Parameters: 
    list_of_numbers (List[int]): a list of integers

Returns: 
    bool: True if all numbers are even

Assumptions: 
    * You can assume that the list is non-empty.

Complexity: 
    Time Complexity: O(N) where N it length of the list. Worst case we need to visit each element in the list, but the program will resolve as soon as an odd element is found.
    Space Complexity: O(1) because the function only stores a single boolean variable regardless of input size.
"""

"""
Scratchpad
* We need to visit each element in the list and confirm if it is even
* We know if an element is even if modulo that number is 0
* As soon as we hit an element that is not odd we can exit as False
""" 

def all_even(list_of_numbers: List[int]) -> bool: 

    for number in list_of_numbers:
        if number % 2 != 0:
            return False
    
    return True

def test_00():
    numbers = [4, 90, 68, 6, -2]
    return all_even(numbers) # -> True

def test_01():
    numbers = [14, 40, 36, 3]
    return all_even(numbers) # -> False

def test_02():
    numbers = [30, 24, 2048, 0, 12, 50]
    return all_even(numbers) # -> True

def test_03():
    numbers = [7, 7, 7, 7]
    return all_even(numbers) # -> False

def test_04():
    numbers = [100]
    return all_even(numbers) # -> True

def test_05():
    numbers = [1, 2, 4, 6, 8]
    return all_even(numbers) # -> False

def test_06():
    numbers = [42, 18, 96, 4, 70, 12, 58, 30, 84, 26]
    return all_even(numbers) # -> True

def test_07():
    numbers = [-5, -3, -4]
    return all_even(numbers) # -> False

### EXECUTE TESTS
print(test_runner(test_00, True))
print(test_runner(test_01, False))
print(test_runner(test_02, True))
print(test_runner(test_03, False))
print(test_runner(test_04, True))
print(test_runner(test_05, False))
print(test_runner(test_06, True))
print(test_runner(test_07, False))