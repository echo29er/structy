
def largest_component(graph): 
    """
    Function Purpose: 
        Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
        The function should return the size of the largest connected component in the graph.
    
    Parameters:
        graph (list): an adjaceny list of an undirected graph.

    Returns:
        int: The size of the largest connected component in the graph i.e. the graph with the most nodes.
        
    Assumptions: 
        N/A

    Time complexity: 
        O(e) number of edges

    Space Complexity: 
        O(n) number of nodes

    """

    """ 
    INITIAL THOUGHTS 
    * We need to build up a dictionary of the edges to create an adjacency list.
    
    
    """
    
    # Handle empty graph
    if not graph: 
        return 0
    
    # Initialise a set to make use of a look up of O(1) and initialise the largest component
    visited = set()
    largest = 0 

    for node in graph: 
        if node not in visited: 
            component_size = explore(graph, node, visited)
            largest = max(largest, component_size)
    
    return largest
    
def explore(graph, current, visited):
    if current in visited: 
        return 0 # already visited so do not count
    
    visited.add(current)
    graph_count = 1

    # Explore and count neighbours
    for neighbour in graph[current]:
        graph_count += explore(graph, neighbour, visited)

    return graph_count


### TEST CASES

def test_a():
    return largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4

def test_b():
    return largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 6

def test_c():
    return largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 5

def test_d():
   return largest_component({}) # -> 0

def test_e():
    return largest_component({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) # -> 3

### EXECUTE TESTS
print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
