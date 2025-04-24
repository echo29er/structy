from test_runner import test_runner
from collections import deque

def closest_carrot(grid, starting_row, starting_column):
    """
    Function Purpose:
        Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column.
        In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots.
        The function should return a number representing the length of the shortest path from the starting position to a carrot.
        You may move up, down, left, or right, but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.

    Parameters:
        * grid (2d array): a list made up of lists that contain 'X's are walls, 'O's are open spaces, and 'C's are carrots.
        * starting_row - an integer denoting the row of the starting cell (starting from 0)
        * starting_column - an integer denoting the column of the starting cell (starting from 0)

    Returns:
        int: the length of the shortest path from the starting position to a carrot

    Assumptions:
        * If there is no possible path to a carrot, then return -1.

    Time complexity:
        O(rc) product of the number of rows and columns

    Space Complexity:
        O(rc) product of the number of rows and columns
    """
    # Handle the empty grid
    if not grid or not grid[0]:
        return -1

    # Construct the grid
    rows, columns = len(grid), len(grid[0])

    # Initialise queue and visited set
    queue = deque([(starting_row, starting_column, 0)])
    visited = {(starting_row, starting_column)}

    # Breadth first search
    while queue:
        row, column, distance = queue.popleft()

        # Check if a carrot has been found
        if grid[row][column] == "C":
            return distance

        # Check all four directions
        directions = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]

        for neighbor_row, neighbor_col in directions:
            # Check if valid neighbor
            if (0 <= neighbor_row < rows and
                0 <= neighbor_col < columns and
                grid[neighbor_row][neighbor_col] != 'X' and
                (neighbor_row, neighbor_col) not in visited):

                # Add to queue and mark as visited
                queue.append((neighbor_row, neighbor_col, distance + 1))
                visited.add((neighbor_row, neighbor_col))

    # If no carrot found
    return -1

### TEST CASES
def test_00():
  grid = [
      ['O', 'O', 'O', 'O', 'O'],
      ['O', 'X', 'O', 'O', 'O'],
      ['O', 'X', 'X', 'O', 'O'],
      ['O', 'X', 'C', 'O', 'O'],
      ['O', 'X', 'X', 'O', 'O'],
      ['C', 'O', 'O', 'O', 'O'],
]
  return closest_carrot(grid, 1, 2) # -> 4

def test_01():
  grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
  ]
  return closest_carrot(grid, 0, 0) # -> 5

def test_02():
  grid = [
    ['O', 'O', 'X', 'X', 'X'],
    ['O', 'X', 'X', 'X', 'C'],
    ['O', 'X', 'O', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'C', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
  ]

  return closest_carrot(grid, 3, 4) # -> 9

def test_03():
  grid = [
    ['O', 'O', 'X', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'C', 'C', 'O'],
  ]

  return closest_carrot(grid, 1, 4) # -> 2

def test_04():
  grid = [
    ['O', 'O', 'X', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'C', 'C', 'O'],
  ]

  return closest_carrot(grid, 2, 0) # -> -1

def test_05():
  grid = [
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'C'],
  ]

  return closest_carrot(grid, 0, 0) # -> -1

def test_06():
  grid = [
  ['O', 'O', 'X', 'C', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['C', 'X', 'O', 'O', 'O'],
]

  return closest_carrot(grid, 2, 2) # -> 5

### EXECUTE TESTS
print(test_runner(test_00, 4))
print(test_runner(test_01, 5))
print(test_runner(test_02, 9))
print(test_runner(test_03, 2))
print(test_runner(test_04, -1))
print(test_runner(test_05, -1))
print(test_runner(test_06, 5))