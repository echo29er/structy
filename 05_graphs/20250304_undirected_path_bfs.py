from collections import deque

def has_path(graph, source, destination): 
    """
    Function Purpose: 
        Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (source, destination). 
        The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.
    
    Parameters:
        graph (dictionary): the dictionary where key values are nodes, and values are a list of adjacent nodes.
        source (str): the node represented as a string where we start in the graph. 
        destination (str): the node represented as a string where we end in the graph. 

    Returns:
        bool: True when there is a direct path between the source and the destination, and False when there is no direct path. 
        
    Assumptions: 
        - The graph is directed acyclic.
        - There is at least one node in the graph.

    Time complexity: 
        O(e) number of edges

    Space Complexity: 
        O(n) number of nodes

    """

    """ 
    INITIAL THOUGHTS 
    * We can use the dictionary. 
    * We check if they key is in the dictionary. 
    * If it isn't then we return False. 
    * If it is then, we check key's value which is an array. 
    
    
    """
    # BREADTH FIRST SEARCH 
    ## Therefore we use a queue

    if source not in graph: 
        return False
    
    # Edge case: source is the destination
    if source == destination:
        return True
    
    # Instantiate and initialise the stack and a set of visited nodes
    queue = deque([source])
    visited = set() 

    while queue: 
        current_node = queue.popleft()
         
        if current_node == destination:
            return True

        if current_node in visited: 
            continue

        visited.add(current_node)

        # Add all neighbours to the stack 
        if current_node in graph: 
            for neighbour in graph[current_node]:
                if neighbour not in visited: 
                    queue.append(neighbour)

    
    return False


### TEST CASES

def test_a():
    graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
    }

    return has_path(graph, 'f', 'k') # True

def test_b():
    graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
    }

    return has_path(graph, 'f', 'j') # False

def test_c():
    graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
    }

    return has_path(graph, 'i', 'h') # True

def test_d():
    graph = {
    'v': ['x', 'w'],
    'w': [],
    'x': [],
    'y': ['z'],
    'z': [],  
    }

    return has_path(graph, 'v', 'w') # True

def test_e():
    graph = {
    'v': ['x', 'w'],
    'w': [],
    'x': [],
    'y': ['z'],
    'z': [],  
    }

    return has_path(graph, 'v', 'z') # False

### EXECUTE TESTS

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())