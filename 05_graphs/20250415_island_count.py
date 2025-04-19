def island_count(grid): 
    """
    Function Purpose: 
        Write a function, island_count, that takes in a grid containing Ws and Ls. 
        W represents water and L represents land. 
        The function should return the number of islands on the grid. 
        An island is a vertically or horizontally connected region of land.
    
    Parameters:
        grid (2d array): a list made up of lists that contain 'W' or 'L'

    Returns:
        int: The number of islands.
        
    Assumptions: 
        * An island is a vertically or horizontally connected region of land. 

    Time complexity: 
        O(e) number of edges

    Space Complexity: 
        O(n) number of nodes

    """

    # Handle the empty gride
    if not grid or not grid[0]:
        return 0
    
    # Construct the grid
    rows, columns = len(grid), len(grid[0]) 
    # As the grid is square the length of grid[0] will return the height
    
    # Instantiate a set to track visited cells
    # A set has o(1) lookup and can only contain unique values
    visited = set() 
    
    # Instantiate a count and initialise it to 0
    count = 0 

    # Helper function to explore an island using DFS
    def explore_island(row, column):
        # Check if position is out of bounds, is water, or already visited
        if ( 
            row < 0 or row >= rows or column < 0 or column >= columns 
            or 
            grid[row][column] == 'W' 
            or 
            (row, column) in visited):
            return
        
        visited.add((row, column))

        # Explore in four directions (up, down, left, right)
        explore_island(row - 1, column) # Up
        explore_island(row + 1, column) # Down
        explore_island(row, column - 1) # Left
        explore_island(row, column + 1) # Right
        
    # Iterate through each cell in the grid
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 'L' and (row, column) not in visited:
                count += 1 # Found a new island
                explore_island(row, column) # Mark all cells in this island as visited

    return count

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
    return island_count(grid) # -> 3

def test_b():
    grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]
    return island_count(grid) # -> 4

def test_c():
    grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]
    return island_count(grid) # -> 1

def test_d():
   grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
  ]
   return island_count(grid) # -> 0

### EXECUTE TESTS
print(test_a())
print(test_b())
print(test_c())
print(test_d())