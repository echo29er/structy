# To test the speed of the tests
import time

def minimum_island(grid): 
    """
    Function Purpose: 
        Write a function, minimum_island, that takes in a grid containing Ws and Ls. 
        W represents water and L represents land. The function should return the size of the smallest island. 

        You may assume that the grid contains at least one island.
    
    Parameters:
        grid (2d array): a list made up of lists that contain 'W' or 'L'

    Returns:
        int: The size of smallest island. 
        
    Assumptions: 
        * An island is a vertically or horizontally connected region of land. 

    Time complexity: 
        O(rc) product of the number of rows and columns

    Space Complexity: 
        O(rc) product of the number of rows and columns

    """

    # Handle the empty gride
    if not grid or not grid[0]:
        return 0
    
    # Instantiate a sentinel - initialised to infinity
    minimum_size = float('inf')
    
    # Construct the grid
    rows, columns = len(grid), len(grid[0]) 
    # As the grid is square the length of grid[0] will return the height
    
    # Instantiate a set to track visited cells
    # A set has o(1) lookup and can only contain unique values
    visited = set()

    # Helper function to explore an island using DFS
    def explore_island(row, column):
        # Base casese: Check if position is out of bounds, is water, or already visited
        if ( 
            row < 0 or row >= rows or column < 0 or column >= columns 
            or 
            grid[row][column] == 'W' 
            or 
            (row, column) in visited):
            return 0
        
        # Count the current cell
        visited.add((row, column))
        size = 1

        # Explore in four directions (up, down, left, right) and sum their results

        size += explore_island(row - 1, column) # Up
        size += explore_island(row + 1, column) # Down
        size += explore_island(row, column - 1) # Left
        size += explore_island(row, column + 1) # Right

        return size
    # Iterate through each cell in the grid
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 'L' and (row, column) not in visited:
                # Declare a new variable to initalise it with the value returned by explore_island
                # This will work recursively.
                current_island_size = explore_island(row, column)
                minimum_size = min(current_island_size, minimum_size)

    return minimum_size

### TEST RUNNER
def test_runner(test_function, expected_result):
    """
    Runs a test function with timing and verification
    
    Args:
        test_name: Name of the test for identification
        test_func: Function to execute (should take no arguments)
        expected_result: The expected result
        
    Returns:
        String with test result and timing information
    """
    test_name = test_function.__name__  # Get the function name automatically
    start_time = time.perf_counter()
    actual = test_function()
    execution_time = time.perf_counter() - start_time
    
    # Convert to microseconds for better precision with fast tests
    execution_time_us = execution_time * 1_000_000

    try:
        assert actual == expected_result, f"Expected {expected_result}, got {actual}"
        return f"✓ {test_name}: PASS - Result: {actual} (executed in {execution_time_us:.2f} microseconds)"
    except AssertionError as e:
        return f"✗ {test_name}: FAIL - {e} (executed in {execution_time_us:.2f} microseconds)"


### TEST CASES
def test_a():
    grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
    return minimum_island(grid)

def test_b():
    grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]
    return minimum_island(grid)


def test_c():
    grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]
    return minimum_island(grid)


def test_d():
    grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]
    return minimum_island(grid)


### EXECUTE TESTS
print(test_runner(test_a, 3))
print(test_runner(test_b, 1))
print(test_runner(test_c, 9))
print(test_runner(test_d, 1))