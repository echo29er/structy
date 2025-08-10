from test_runner import test_runner
from typing import Dict, List

def longest_path(graph: Dict[str, List[str]]) -> int:
    """
    Function Purpose:
        Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. 
        The function should return the length of the longest path within the graph. 
        A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes. 

    Parameters:
        * graph - an adjacency list for a directed acyclic graph.

    Returns:
        int: the length of the longest path within the graph.

    Assumptions:
        * A path may start and end at any two nodes.

    Time complexity:
        O(e) # traversal through the entire graph

    Space Complexity:
        O(n) # will mark all nodes as visited
    """
    # Handle the empty graph
    if not graph:
        return 0

    # Topological sort 
    # Need a function to compute the topological order of nodes. 
    # We use DFS. Each node is added to the stack after all its children are processed. 
    def topological_sort(graph):
        # Instantiate a set to make use of a look up of O(1) and a stack
        visited = set()
        stack = []

        for node in graph: 
            if node not in visited: 
                dfs(node, visited, stack, graph)

        return stack[::-1] # Reverse the order
    
    def dfs(current_node, visited, stack, graph):
        # Marks the current node as visited
        # Recursively visits all the unvisited neighbours
        # After all neighbours and their subtrees are processed, adds the current node to the stack
        # This creates a post-order traversal where nodes are added to the stack when all descendants 
        # have been processed
        visited.add(current_node)
        for neighbour in graph[current_node]:
            if neighbour not in visited:     
                dfs(neighbour, visited, stack, graph)
        stack.append(current_node)
            
    # Calculate longest path
    topological_order = topological_sort(graph)
    distances = {node: 0 for node in graph} # initialise dictionary with key=node and value=0

    for node in topological_order:
        for neighbour in graph[node]:
            distances[neighbour] = max(distances[neighbour], distances[node]+1) # distance[node]+1 calculates the distance betwen the node and neighbour

    # Find the maximum distance
    return max(distances.values()) if distances else 0

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