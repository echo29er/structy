from test_runner import test_runner
from typing import Dict, List

def longest_path(graph: Dict[str, List[str]]) -> int:
    """
    Function Purpose:
        Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. 
        The function should return the length of the longest path within the graph. 
        A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes. 

    Parameters:
        * graph - an adjacency list for a directec acyclic graph.

    Returns:
        int: the length of the longest path within the graph.

    Assumptions:
        * A path may start and end at any two nodes.

    Time complexity:
        O(e) # traversal through the entire graph

    Space Complexity:
        O(n) # will mark all nodes as visited
    """
    
    # Locate terminal nodes -> a dead end is a 0 edge path
    # Store these distances from terminal nodes in a dictionary. This also tells you nodes visited.
    # Initialize distances dictionary outside of any conditional blocks
    distances = {}

    for node in graph: # check if neighbours are 0 i.e. is terminal
        if len(graph[node]) == 0: 
            distances [node] = 0

    # Execute a depth first traversal after all terminal nodes found
    for node in graph: 
        traverse_distance(graph, node, distances)

    return max(distances.values()) if distances else 0

# write the dfs
def traverse_distance(graph, node, distances):
    if node in distances: 
        return distances[node] # if we already know this node's longest path, return it

    # Otherwise, calculate the path length
    max_length = 0

    # Ask each neighbour about their longest path
    for neighbour in graph[node]:
        new_length = traverse_distance(graph, neighbour, distances)
        
        # Keep track of the best neighbor
        if new_length > max_length:
            max_length = new_length

    # Our longest path is the edge to our best neighbour (1) plus their longest path
    # Save this result so we don't recalculate it
    distances[node] = 1 + max_length # return the length at the node rather than the neighbour
    # i.e. 1 plus the node you're

    return distances[node]


### TEST CASES
def test_00():
    graph = {
    'a': ['c', 'b'],
    'b': ['c'],
    'c': []
    }

    return longest_path(graph) # -> 2

def test_01():
    graph = {
    'a': ['c', 'b'],
    'b': ['c'],
    'c': [],
    'q': ['r'],
    'r': ['s', 'u', 't'],
    's': ['t'],
    't': ['u'],
    'u': []
    }

    return longest_path(graph) # -> 4

def test_02():
    graph = {
    'h': ['i', 'j', 'k'],
    'g': ['h'],
    'i': [],
    'j': [],
    'k': [],
    'x': ['y'],
    'y': []
    }

    return longest_path(graph) # -> 2

def test_03():
    graph = {
    'a': ['b'],
    'b': ['c'],
    'c': [],
    'e': ['f'],
    'f': ['g'],
    'g': ['h'],
    'h': []
    }

    return longest_path(graph) # -> 3

def test_04():
    graph = {
    'a': ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'b': ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'c': ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'd': ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'e': ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'f': ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    'g': ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    'h': ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    'i': ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    'j': ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
    'k': ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
    'l': ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
    'm': ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
    'n': ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'o': ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
    'p': ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
    'q': ['r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
    'r': ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    's': ['t', 'u', 'v', 'w', 'x', 'y', 'z'],
    't': ['u', 'v', 'w', 'x', 'y', 'z'],
    'u': ['v', 'w', 'x', 'y', 'z'],
    'v': ['w', 'x', 'y', 'z'],
    'w': ['x', 'y', 'z'],
    'x': ['y', 'z'],
    'y': ['z'],
    'z': []
    }

    return longest_path(graph) # -> 25

### EXECUTE TESTS
print(test_runner(test_00, 2))
print(test_runner(test_01, 4))
print(test_runner(test_02, 2))
print(test_runner(test_03, 3))
print(test_runner(test_04, 25))