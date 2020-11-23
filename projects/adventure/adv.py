from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Queue, Stack

import multiprocessing

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def generate_path():

    graph = {}

    visited = set()

    the_path = []

    def dft(room):
        current_room = room
        previous = None

        while len(graph.keys()) < len(room_graph):
            exits = current_room.get_exits()
            # print('pre add visited', visited)

            if current_room.id not in visited:
                print('FRESH ID', current_room.id)
                for exit in exits:
                    # print('exit', exit)
                    # print('initial graph', graph)
                    if current_room.id in graph:
                        graph[current_room.id][exit] = None
                        # print('yes in graph', graph)
                    else:
                        graph[current_room.id] = {exit: None}
                        # print('NOT in graph', graph)


            visited.add(current_room.id)
            # print('post add visited', visited)

            if previous:
                if previous[0] == "n":
                    graph[current_room.id]["s"] = previous[1]
                if previous[0] == "s":
                    graph[current_room.id]["n"] = previous[1]
                if previous[0] == "e":
                    graph[current_room.id]["w"] = previous[1]
                if previous[0] == "w":
                    graph[current_room.id]["e"] = previous[1]
            print('previous', previous)

            not_attempted = [exit for exit in exits if graph[current_room.id][exit] is None]
            # print('not attempted', not_attempted)

            if len(not_attempted) == 0:
                # print('CURRENT', current_room)
                return current_room

            direction = random.choice(not_attempted)
            # print('new direction', direction)

            the_path.append(direction)
            # print('THE path', the_path)
            new_room = current_room.get_room_in_direction(direction)
            graph[current_room.id][direction] = new_room.id
            previous = [direction, current_room.id]
            current_room = new_room

    def bfs(starting_room):
        paths_dict = {}
        todo = []
        completed = set()

        todo.append([starting_room])
        while len(todo) > 0 and len(graph.keys()) < len(room_graph):
            rooms = todo.pop(0)
            current_room = rooms[-1]
            print('current bfs room', current_room)

            if current_room.id not in completed:
                if None in graph[current_room.id].values():
                    the_path.extend(paths_dict[current_room.id])
                    return current_room
                completed.add(current_room.id)
                print('completed bfs', completed)

                exits = current_room.get_exits()

                for exit in exits:
                    next_room = current_room.get_room_in_direction(exit)
                    if current_room.id in paths_dict:
                        next_room_path = list(paths_dict[current_room.id])
                        next_room_path.append(exit)
                        paths_dict[next_room.id] = next_room_path
                    else:
                        paths_dict[next_room.id] = [exit]
                    new_rooms = list(rooms)
                    new_rooms.append(next_room)
                    todo.append(new_rooms)
                    print('todo bfs', todo)

    current_room = player.current_room

    while len(graph.keys()) < len(room_graph):
        dft_last_room = dft(current_room)

        bfs_last_room = bfs(dft_last_room)

        current_room = bfs_last_room

    print('THE PATH', the_path)
    return the_path



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# if __name__ == "__main__":
#     test_traversal()
#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


