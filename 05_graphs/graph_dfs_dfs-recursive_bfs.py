from collections import deque

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
    

def depth_first_print(graph, starter_node):

    # Instantiate and initialise a stack
    stack = [starter_node]

    while stack: 
        current_node = stack.pop()
        print(current_node)

        # add neighbours
        for neighbour in graph[current_node]:
            stack.append(neighbour)


#depth_first_print(graph, "a")
# Output visalised: https://treeconverter.com/?input=[[%22a%22,%22b%22],+[%22a%22,%22c%22],+[%22b%22,%22d%22],+[%22c%22,%22e%22],[%22d%22,+%22f%22]]


def depth_first_recursive_print(graph, current):

    print(current)
    for neighbour in graph[current]:
        depth_first_recursive_print(graph, neighbour)


# depth_first_recursive_print(graph, "a")
# Output visalised: https://treeconverter.com/?input=[[%22a%22,%22b%22],+[%22a%22,%22c%22],+[%22b%22,%22d%22],+[%22c%22,%22e%22],[%22d%22,+%22f%22]]


def breadth_first_print(graph, starter_node): 

    # Instantiate and initialise a queue and pointer
    queue = [starter_node]
    pointer = 0

    while pointer < len(queue): # while the pointer is less than the length of the queue
        current_node = queue[pointer]
        print(current_node)

        # add neighbours
        for neighbour in graph[current_node]:
            queue.append(neighbour)

        pointer += 1

#breadth_first_print(graph, "a")
# Output visalised: https://treeconverter.com/?input=[[%22a%22,%22b%22],+[%22a%22,%22c%22],+[%22b%22,%22d%22],+[%22c%22,%22e%22],[%22d%22,+%22f%22]]

def breadth_first_deque_print(graph, starter_node): 

    # Instantiate and initialise a queue and pointer
    queue = deque([starter_node])

    while queue: # while queue has nodes
        current_node = queue.popleft()
        print(current_node)

        # add neighbours
        for neighbour in graph[current_node]:
            queue.append(neighbour)

breadth_first_deque_print(graph, "a")
# Output visalised: https://treeconverter.com/?input=[[%22a%22,%22b%22],+[%22a%22,%22c%22],+[%22b%22,%22d%22],+[%22c%22,%22e%22],[%22d%22,+%22f%22]]