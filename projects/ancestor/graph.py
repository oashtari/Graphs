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