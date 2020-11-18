from graph import Graph 

def earliest_ancestor(ancestors, starting_node):

    graph = Graph()

    for (p,c) in ancestors:

        if not graph.vertex_exists(p):
            graph.add_vertex(p)
        if not graph.vertex_exists(c):
            graph.add_vertex(c)

        graph.add_edge(c,p)
    
    neighboring_ancestor = graph.get_neighbors(starting_node)

    if len(neighboring_ancestor) == 0:
        return -1
    
    current = starting_node

    while len(graph.get_neighbors(current)) > 0:
        neighboring_ancestor = graph.get_neighbors(current)

        ancestor = min(neighboring_ancestor)

        current = ancestor

    return current


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1)) 
print(earliest_ancestor(test_ancestors, 4)) 
print(earliest_ancestor(test_ancestors, 6)) 
print(earliest_ancestor(test_ancestors, 9)) 

# MASTER SOLUTION

def earliest_ancestor_master(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        graph.add_edge(pair[1], pair[0])
    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    # q = [[6, 3], [6, 5]]
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor