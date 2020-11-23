islands = [ [0,1,0,1,0],
            [1,1,0,1,1],
            [0,0,1,0,0],
            [1,0,1,0,0],
            [1,1,0,0,0]]

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

def islands_counter(islands):
    visited = set()
    counter = 0

    def get_neighbors(coords):
        neighbors = []

        row, col = coords #destructure

        if row > 0 and islands[row-1][col] == 1:
            neighbors.append((row-1, col))
        if row < len(islands) - 1 and islands[row+1][col] == 1:
            neighbors.append((row+1, col))
        if col > 0 and islands[row][col-1] == 1:
            neighbors.append((row, col-1))
        if col < len(islands[row]) -1 and islands[row][col+1] == 1:
            neighbors.append((row, col+1))

        return neighbors

    def bft(row, col):
        q = Queue()

        q.enqueue((row,col))

        while q.size() > 0:
            coords = q.dequeue()

            if coords not in visited:
                visited.add(coords)

                for neighbor in get_neighbors(coords):
                    q.enqueue(neighbor)



    # for all nodes in graph
    for row in range(len(islands)):
        for col in range(len(islands[row])):
            node_val = islands[row][col]
            
            coords = (row, col)

        # if we find an univisted 1 node:
            if coords not in visited and node_val == 1:

            # bft from that node
                bft(row,col)

            #increment our counter
                counter +=1 
    # return counter
    return counter

print (islands_counter(islands) )# returns 4



# TIM'S SOLUTION

# """
# Write a function that takes a 2D binary array and returns the number of 1 islands. 
# ​
# An island consists of 1s that are connected to the north, south, east or west. For example:
# ​
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# ​
# island_counter(islands) # returns 4
# ​
# 1. Describe the problem in graphs terms
# -- What are our nodes?
# --- each (x, y) in the array 
# ---- if it's a 1? or we only operate on the 1s
# ​
# -- What are our edges? when are nodes connected?
# --- connected when a direct neighbor is a 1
# ​
# -- Island in graphs terms?
# --- connected component
# ​
# 2. Build your graph or write getNeighbors
# ​
# -- go through the array node by node, then check north, east, south, west 
# neighbors are like.. index - 1[same place], index[-1 place], index[+1 place], index + 1[same place]
# ​
# 3. Choose your fighter(s)
# ​
# -- How to count the number of connected components?
# -- get to each island, traverse the component, then continue from where you were
# --- keep track of which nodes have already been traversed
# ​
# ​
# -- go through the array node by node, then check north, east, south, west 
# """
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# ​
# big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#                [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#                [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#                [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#                [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#                [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#                [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#                [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#                [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#                [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
# # 13 big islands!!
# ​
# # getNeighbors goes here
# def getNeighbors(row, col, matrix):
# # check north, east, south, west 
# # neighbors are like.. index - 1[same place], index[-1 place], index[+1 place], index + 1[same place]
# # What about the edges of the matrix?
# # check if these are 1s
# ​
#     neighbors = []
# ​
#     if col >= 1:
#         west_neighbor = matrix[row][col - 1]
#         if west_neighbor == 1:
#             neighbors.append((row, col - 1))
# ​
#     if col <= len(matrix) - 2:
#         east_neighbor = matrix[row][col + 1]
#         if east_neighbor == 1:
#             neighbors.append((row, col + 1))
# ​
#     if row <= len(matrix) - 2:
#         south_neighbor = matrix[row + 1][col]
#         if south_neighbor == 1:
#             neighbors.append((row + 1, col))
# ​
#     if row >= 1:
#         north_neighbor = matrix[row - 1][col]
#         if north_neighbor == 1:
#             neighbors.append((row - 1, col))
# ​
#     return neighbors
# ​
# # traversal goes here
# def dft_recursive(row, col, visited, matrix):
#     if (row, col) not in visited:
#         visited.add((row, col))
# ​
#         neighbors = getNeighbors(row, col, matrix)
# ​
#         for neighbor in neighbors:
#             dft_recursive(neighbor[0], neighbor[1], visited, matrix)
# ​
# # count number of connected components
# def count_islands(matrix):
#     visited = set()
# ​
#     number_of_connected_components = 0
# ​
#     # iterate over the matrix
#     for row in range(len(matrix)):
#         for col in range(len(matrix)):
#             node = matrix[row][col]
#     # if 0 continue, 
#             if node == 0:
#                 continue
#     # if 1: hold place, traverse and add each to visited, at end go back
#             elif node == 1:
#                 if (row, col) not in visited:
#                     number_of_connected_components += 1
# ​
#                     dft_recursive(row, col, visited, matrix)
# ​
#     return number_of_connected_components
# ​
# ​
# ​
# print(count_islands(islands)) # return 4