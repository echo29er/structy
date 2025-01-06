# Problem: Given a list of numbers and a target, write a function that returns a tuple containing a pair of indices whose elements sum to the given target

def pair_sum(numbers, target):


# # o(n^2) approach where a loop is in a loop
#     for index in range(len(numbers)):
#         for index_plus_one in range(index+1,len(numbers)):
#             if numbers[index]+numbers[index_plus_one] == target:
#                 return(index, index_plus_one)


# o(n) approach using a hash map
    complement_dictionary = {}
    for index, number in enumerate(numbers):
        complement = target - number

        if complement in complement_dictionary:
            return (index, complement_dictionary[complement])
        
        complement_dictionary[number] = index









# Test variables
test_numbers = [1,2,3,4,5,6]
target_sum = 8

print(pair_sum(test_numbers, target_sum))