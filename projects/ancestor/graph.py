class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v_from, v_to):
        """
        Add a directed edge to the graph.
        """
        if v_from in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)
        else:
            raise IndexError('nonexistent vertex')

    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def vertex_exists(self, vertex_id):
        """
        Return validity of vertex_id in graph instance
        """
        if vertex_id in self.vertices:
            return True
        else:
            return False

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()
        visited = set()

        q.push(starting_vertex)

        while q.size() > 0:
            v = q.pop()

            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)
    

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        print(starting_vertex)
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()

        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()
            
            v = path [-1]

            if v not in visited:
                if v == destination_vertex:
                    return path

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    new_path = path + [neighbor]
                    q.enqueue(new_path)

        return None



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        q = Stack()
        visited = set()

        q.push([starting_vertex])

        while q.size() > 0:
            path = q.pop()
            v = path[-1]

            if v not in visited:
                if v == destination_vertex:
                    return path

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    new_path = path + [neighbor]
                    q.push(new_path)

        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = [starting_vertex]

        print(starting_vertex)
        visited.add(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:

                new_path = path + [neighbor]
                if neighbor == destination_vertex:
                    return new_path
                dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if dfs_path is not None:
                    return dfs_path
        return None 



# TIM'S SOLUTION

# """
# ​
# DFT/DFS vs BFT/BFS
# ​
# When is DFS better?
# - might find the longest path
# - if the node you're looking is a leaf
# - can also be implemented recursively, or randomly
# ​
# When is BFS better?
# - finds shortest path
# ​
# ​
# Simple graph implementation
# """
# from util import Stack, Queue  # These may come in handy
# ​
# class Graph:
# ​
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
# ​
#     def add_vertex(self, vertex_id):
#         """
#         Add a vertex to the graph.
#         """
#         self.vertices[vertex_id] = set()
# ​
#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError("All your vertices are mine, or rather, do not exist.")
# ​
#     def get_neighbors(self, vertex_id):
#         """
#         Get all neighbors (edges) of a vertex.
#         """
#         return self.vertices[vertex_id]
# ​
#     def bft(self, starting_vertex):
#         """
#         Print each vertex in breadth-first order
#         beginning from starting_vertex.
#         """
#         # make a queue
#         q = Queue()
# ​
#         # make a set to track which nodes we have visited
#         visited = set()
# ​
#         # enqueue the starting node
#         q.enqueue(starting_vertex)
# ​
#         # loop while the queue isn't empty
#         while q.size() > 0:
#             # dequeue, this is our current node
#             current_node = q.dequeue()
# ​
#             # check if we've yet visited
#             if current_node not in visited:
#                 print(current_node)
#             ## if not, we go to the node
#             ### mark as visited == add to visited set
#                 visited.add(current_node)
# ​
#             ### get the neighbors
#                 neighbors = self.get_neighbors(current_node)
#             ### iterate over the neighbors, enqueue them
#                 for neighbor in neighbors:
#                     q.enqueue(neighbor)
# ​
# ​
#     def dft(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """
#         # make a queue
#         stack = Stack()
# ​
#         # make a set to track which nodes we have visited
#         visited = set()
# ​
#         # push on the starting node
#         stack.push(starting_vertex)
# ​
#         # loop while the stack isn't empty
#         while stack.size() > 0:
#             # pop, this is our current node
#             current_node = stack.pop()
# ​
#             # check if we've yet visited
#             if current_node not in visited:
#                 print(current_node)
#             ## if not, we go to the node
#             ### mark as visited == add to visited set
#                 visited.add(current_node)
# ​
#             ### get the neighbors
#                 neighbors = self.get_neighbors(current_node)
#             ### iterate over the neighbors, enqueue them
#                 for neighbor in neighbors:
#                     stack.push(neighbor)
# ​
#     def dft_recursive(self, vertex, visited=set()):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
# ​
#         This should be done using recursion.
# ​
#         # need a base case
# ​
#         # needs to call itself
#         """
#         if vertex not in visited:
#             print(vertex)
# ​
#             visited.add(vertex)
# ​
#             neighbors = self.get_neighbors(vertex)
#             if len(neighbors) == 0:
#                 return
# ​
#             else:
#                 for neighbor in neighbors:
#                     self.dft_recursive(neighbor, visited)
# ​
# ​
# ​
#     def bfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
# ​
#         1. stop when we find the target node
# ​
#         2. return the path we took to get there
#         -  note, this will automatically be the shortest path
# ​
#         Enqueue a PATH TO the starting node, instead of just the starting node
#         """
#         # make a queue
#         q = Queue()
# ​
#         # make a set to track which nodes we have visited
#         visited = set()
# ​
#         # enqueue the PATH TO the starting node
#         q.enqueue([starting_vertex])
# ​
#         # loop while the queue isn't empty
#         while q.size() > 0:
#             # dequeue, this is our current path
#             current_path = q.dequeue()
#             current_node = current_path[-1]
# ​
#             # check if we have found our target node
#             if current_node == destination_vertex:
#                 # then we are done! return
#                 return current_path
# ​
#             # check if we've yet visited
#             if current_node not in visited:
#             ## if not, we go to the node
#             ### mark as visited == add to visited set
#                 visited.add(current_node)
# ​
#             ### get the neighbors
#                 neighbors = self.get_neighbors(current_node)
#             ### iterate over the neighbors, enqueue the PATH to them
#                 for neighbor in neighbors:
#                     # path_copy = list(current_path)
#                     # path_copy = current_path.copy()
#                     # path_copy = copy.copy(current_path)
#                     # path_copy = current_path[:]
# ​
#                     # path_copy.append(neighbor)
#                     path_copy = current_path + [neighbor]
# ​
#                     q.enqueue(path_copy)
# ​
# ​
#     def dfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.
# ​
#         will not necessarily be the shortest path!!
#         """
#         pass  # TODO
# ​
#     def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.
# ​
#         This should be done using recursion.
#         """
#         if len(path) == 0:
#             path.append(starting_vertex)
# ​
#         if starting_vertex == destination_vertex:
#             return path
# ​
#         if starting_vertex not in visited:
#             visited.add(starting_vertex)
        
#             neighbors = self.get_neighbors(starting_vertex)
# ​
#             for neighbor in neighbors:
#                 path_copy = path + [neighbor]
# ​
#                 # only return if we found the destination_vertex
# ​
#                 result = self.dfs_recursive(neighbor, destination_vertex, path_copy, visited)
#                 if result is not None:
#                     return result
# ​
# ​
# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)
# ​
#     '''
#     starting_vertex: 1
#     destination_vertex: 5
# ​
#     q = Queue()
#     visited = set()
# ​
#     current_path = [1]
#     current_node = current_path[-1]
# ​
#     1: [1]
#     2: [1, 2]
#     3: [1, 2, 3]
#     5: [1, 2, 3, 5]
    
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)
# ​
#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     graph.bft(1)
# ​
#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     graph.dft(1)
#     graph.dft_recursive(1)
# ​
#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print(graph.bfs(1, 6))
# ​
#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))