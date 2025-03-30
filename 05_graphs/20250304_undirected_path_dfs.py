
def undirected_path(edges, node_a, node_b): 
    """
    Function Purpose: 
        Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
        The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
    
    Parameters:
        edges (list): a list containing edges made from pairs of nodes.
        node_a (str): the node represented as a string where we start in the graph. 
        node_b (str): the node represented as a string where we end in the graph. 

    Returns:
        bool: True when there is a direct path between node_a and node_b, and False when there is no direct path. 
        
    Assumptions: 
        - There is at least one node in the graph.

    Time complexity: 
        O(e) number of edges

    Space Complexity: 
        O(n) number of nodes

    """

    """ 
    INITIAL THOUGHTS 
    * We need to build up a dictionary of the edges to create an adjacency list.
    
    
    """
    # ADJACENCY LIST CONSTRUCTION
    adjacency_list = {}

    for tuple in edges: 
        node_source, node_destination = tuple

        # We need to initialise empty sets (to not have duplicates), we also get the benefit of O(1) look ups.
        if node_source not in adjacency_list: 
            adjacency_list[node_source] = set()
        if node_destination not in adjacency_list: 
            adjacency_list[node_destination] = set()

        # Add the nodes 
        adjacency_list[node_source].add(node_destination)
        adjacency_list[node_destination].add(node_source)

    # DEPTH FIRST SEARCH 
    ## Then we can use a stack to execute depth first search

    if node_a not in adjacency_list or node_b not in adjacency_list: 
        return False
    
    # Edge case: source is the destination
    if node_a == node_b:
        return True
    
    # Instantiate and initialise the stack and a set of visited nodes
    stack = [node_a]
    visited = set() 

    while stack: 
        current_node = stack.pop()
         
        if current_node == node_b:
            return True

        if current_node in visited: 
            continue

        visited.add(current_node)

        # Add all neighbours to the stack 
        if current_node in adjacency_list: 
            for neighbour in adjacency_list[current_node]:
                if neighbour not in visited: 
                    stack.append(neighbour)

    
    return False


### TEST CASES

def test_a():
    edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
    ]

    return undirected_path(edges, 'j', 'm') # -> True

def test_b():
    edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
    ]

    return undirected_path(edges, 'm', 'j') # -> True

def test_c():
    edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
    ]

    return undirected_path(edges, 'l', 'j') # -> True


def test_d():
    edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
    ]

    return undirected_path(edges, 'k', 'o') # -> False


def test_e():
    edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
    ]

    return undirected_path(edges, 'i', 'o') # -> False

def test_f():
    edges = [
    ('b', 'a'),
    ('c', 'a'),
    ('b', 'c'),
    ('q', 'r'),
    ('q', 's'),
    ('q', 'u'),
    ('q', 't'),
    ]


    return undirected_path(edges, 'a', 'b') # -> True


def test_g():
    edges = [
    ('b', 'a'),
    ('c', 'a'),
    ('b', 'c'),
    ('q', 'r'),
    ('q', 's'),
    ('q', 'u'),
    ('q', 't'),
    ]

    return undirected_path(edges, 'a', 'c') # -> True

def test_h():
    edges = [
    ('b', 'a'),
    ('c', 'a'),
    ('b', 'c'),
    ('q', 'r'),
    ('q', 's'),
    ('q', 'u'),
    ('q', 't'),
    ]

    return undirected_path(edges, 'r', 't') # -> True

def test_i():
    edges = [
    ('s', 'r'),
    ('t', 'q'),
    ('q', 'r'),
    ]

    return undirected_path(edges, 'r', 't') # -> True




### EXECUTE TESTS

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
print(test_f())
print(test_g())
print(test_h())
print(test_i())