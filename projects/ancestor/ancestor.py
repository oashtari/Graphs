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