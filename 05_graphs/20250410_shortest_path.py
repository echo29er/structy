from collections import deque

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
        node_B (str): the destination node 

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
    graph = construct_graph(edges)

    # Keep track of visited nodes to avoid cycles
    visited = set([ node_A ])

    # Queue stores tuples of (node, distance_from_start)
    # Using deque for efficient O(1) popleft operations
    queue = deque([ (node_A, 0) ])

    # BFS implementation
    while queue: 
        # Get the next node and its distance from the start
        node, distance = queue.popleft()

        # If we've reached our destination, return the distance
        if node == node_B:
            return distance 
        
        # Explore all unvisited neighbors
        for neighbour in graph[node]:
            if neighbour not in visited: 
                # Mark as visited to avoid cycles
                visited.add(neighbour)
                # Add to queue with incremented distance
                queue.append((neighbour, distance + 1))

    # If we've exhausted all nodes without finding node_B,
    # there is no path between A and B
    return -1

# Create adjaceny list
def construct_graph(edges):
    """
    Convert a list of edges into an adjacency list representation.
    For undirected graphs, each edge is added in both directions.
    """
    graph = {}
    for edge in edges: 
        start, end = edge # unpack the list

        # Ensure both nodes exist as keys in the graph
        if start not in graph: # add key to the dictionary
            graph[start] = []
        if end not in graph: 
            graph[end] = []
        
        graph[start].append(end) # add both edges to the dictionary
        graph[end].append(start)

    return graph

### TEST CASES

def test_a():
    edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
    return shortest_path(edges, 'w', 'z') # -> 2

def test_b():
    edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

    return shortest_path(edges, 'y', 'x') # -> 1

def test_c():
    edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

    return shortest_path(edges, 'a', 'e') # -> 3

def test_d():
    edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]
    return shortest_path(edges, 'e', 'c') # -> 2

def test_e():
    edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

    return shortest_path(edges, 'b', 'g') # -> -1

### EXECUTE TESTS
print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())