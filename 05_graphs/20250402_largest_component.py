
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
    
    # Use a set to give O(1) insertion and look up
    visited = set()
    count = 0 # initialise the count
    biggest_component = 0 # initialise result

    for node in graph: 
        # node is the key of each dictionary
        if explore(graph, node, visited) == True: 
            count += 1
    
    return count
    
def explore(graph, current, visited):
    if current in visited: 
        return False # for a component we've seen
    
    visited.add(current)

    for neighbour in graph[current]:
        explore(graph, neighbour, visited)

    return True


### TEST CASES

def test_a():
    return connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2


def test_b():
    return connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2


def test_c():
    return connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 3



def test_d():
   return connected_components_count({}) # -> 0



def test_e():
    return connected_components_count({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) # -> 5



### EXECUTE TESTS

print(test_a())
print(test_b())
print(test_c())
print(test_d())
print(test_e())
