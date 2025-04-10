def shortest_path(edges, node_A, node_B): 
    """
    Function Purpose: 
        Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
        The function should return the length of the shortest path between node_A and node_B. 
        Consider the length as the number of edges in the path, not the number of nodes. 
        If there is no path between A and B, then return -1. 
    
    Parameters:
        edges (list of lists): a list that contains pairs of nodes each in a list. 
        node_A (str): the source node
        node_B (str)" the destination node 

    Returns:
        int: The number of edges traversed.
        
    Assumptions: 
        * You can assume that A and B exist as nodes in the graph.

    Time complexity: 
        O(e) number of edges

    Space Complexity: 
        O(n) number of nodes

    """

    
    ## APPROACH
    # We don't handle an empty graph
    # We should use a breadth first search using an adjacency list. 
    # The BFS explores nodes level by level.

    ## IMPLEMENTATION
    # Instantiate a queue to track the nodes to visit, a visited set to avoid cycels, and a dictionary to keep track of the distance. 

    
    
    
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
