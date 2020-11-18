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
    def __init__(self):
        self.vertices = {} # keys are all the verts in the graph, values are set of verts

    def add_vertex(self, vertex):
        # add a new unconnected vert
        self.vertices[vertex] = set()

    def add_edge(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)
        else:
            raise IndexError("nonexistent vertex")

    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, v):
        return self.vertices[v]

    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()

        # Init:
        q.enqueue(starting_vertex_id)

        # while queue isn't empty:
        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v) # 'visit' the node
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        q = Stack()
        visited = set()

        # Init:
        q.push(starting_vertex_id)

        # while stack isn't empty:
        while q.size() > 0:

            v = q.pop()

            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)

    def bfs(self, starting_vertex_id, target_vertex_id): #breadth first search
        q = Queue()
        visited = set()

        #Init
        q.enqueue([starting_vertex_id])

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty:
        while q.size() > 0:

            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            # end_of_path_node = path[-1] # too verbose, hence use v
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:

                # CHECK IF IT'S THE TARGET
                if v == target_vertex_id:
                    # IF SO, RETURN PATH
                    return path # found it
                
                # Mark it as visited
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    # q.enqueue(neighbor) #actually want to queue the path to get here

                # Then add A PATH TO its neighbors to the back of the queue
                    # COPY THE PATH
                    new_path = path + [neighbor] #creating a new list, by appending the neighbor to the end
                    # new_path = path[:] #using slice notation instead
                    # APPEND THE NEIGHBOR TO THE BACK
                    q.enqueue(new_path)

        return None

# same as change above for using stack
    def dfs(self, starting_vertex_id, target_vertex_id): #breadth first search
        q = Stack()
        visited = set()

        #Init
        q.enqueue([starting_vertex_id])

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty:
        while q.size() > 0:

            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            # end_of_path_node = path[-1] # too verbose, hence use v
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:

                # CHECK IF IT'S THE TARGET
                if v == target_vertex_id:
                    # IF SO, RETURN PATH
                    return path # found it
                
                # Mark it as visited
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    # q.enqueue(neighbor) #actually want to queue the path to get here

                # Then add A PATH TO its neighbors to the back of the queue
                    # COPY THE PATH
                    new_path = path + [neighbor] #creating a new list, by appending the neighbor to the end
                    # new_path = path[:] #using slice notation instead
                    # APPEND THE NEIGHBOR TO THE BACK
                    q.enqueue(new_path)

        return None


    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()

        print(starting_vertex)
        visited.add(starting_vertex) # each new call has a new starting vertex since we're using the neighbor to 'start'

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited: #only want to recurse to unvisited neighbors
                self.dft_recursive(neighbor, visited)

    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
        if visited is None:
            visited = set()

        if path is None:
            path = [starting_vertex]

        print(starting_vertex)
        visited.add(starting_vertex) 

        # path += [starting_vertex] # copy the path, basically sharing a new path with each recursive call

        if starting_vertex == target_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited: #only want to recurse to unvisited neighbors
                
                new_path = path + [neighbor]
                if neighbor == target_vertex:
                    return new_path

                dfs_path = self.dfs_recursive(neighbor, target_vertex, visited, new_path)
                if dfs_path is not None:
                    return dfs_path

        return None

g = Graph()
# g.add_vertex(1)
# g.add_vertex(2)
# g.add_vertex(3)

# g.add_edge(2, 1)
# g.add_edge(1, 2) # to make undirectional graph
# g.add_edge(2, 3)
# print(g.vertices)

# g.bft(1)
# g.bft(2)

# g.dft(2)

# print(g.bfs(1,3))
# print(g.bfs(2,3))
# print(g.bfs(1,2))
# print(g.bfs(3,1))

# new graph for recursive tests
g.add_vertex('A')
g.add_vertex('y')
g.add_vertex('x')
g.add_vertex('z')

g.add_edge('A', 'x')
g.add_edge('x', 'A')
g.add_edge('A', 'y')
g.add_edge('y', 'z')
g.add_edge('z', 'x')
print(g.vertices)

# g.dft_recursive('A')
print(g.dfs_recursive('A', 'z'))