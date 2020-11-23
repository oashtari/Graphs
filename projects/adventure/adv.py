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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
                # print('FRESH ID', current_room.id)
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
            # print('previous', previous)

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
            # print('current bfs room', current_room)

            if current_room.id not in completed:
                if None in graph[current_room.id].values():
                    the_path.extend(paths_dict[current_room.id])
                    return current_room
                completed.add(current_room.id)
                # print('completed bfs', completed)

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
                    # print('todo bfs', todo)

    current_room = player.current_room

    while len(graph.keys()) < len(room_graph):
        dft_last_room = dft(current_room)

        bfs_last_room = bfs(dft_last_room)

        current_room = bfs_last_room

    # print('THE PATH', the_path)
    return the_path

while True:
    path = generate_path()
    if len(path) < 975:
        traversal_path = path
        break

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





# def try_traversal(test = True):

#     # graph = {}
    
#     visited = {}

#     traversal_path = []

#     back_track = []

#     recent_room = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

#     # rooms and exits
#     visited[player.current_room.id] = player.current_room.get_exits()
#     print('visited', visited)

#     # trying to reach 500 rooms
#     while len(visited) < len(room_graph):

#         # unvisited rooms
#         if player.current_room.id not in visited:
#             exits = player.current_room.get_exits()
#             exits.remove(recent_room[traversal_path[-1]])
#             visited[player.current_room.id] = exits 

#         if len(visited[player.current_room.id]) == 0:
#             last_step_direction = back_track.pop()

#             traversal_path.append(last_step_direction)
#             player.travel(last_step_direction)

#         else:
#             available_paths = len(visited[player.current_room.id])
#             direcion_index = (random.randint(0, available_paths-1) if available_paths > 0 else 0)
#             direction = visited[player.current_room.id][direcion_index]

#             visited[player.current_room.id].pop(direcion_index)

#             player.travel(direction)

#             traversal_path.append(direction)

#             back_track.append(recent_room[direction])

#         if test:
#             return traversal_path
#         else:
#             return len(traversal_path)

# def least_steps(walker, attempts, progress, result):
#     steps = []
#     completed = 0
#     print_progress = attemps * (progress/100)

#     print("here we go...")

#     for i in range(0,attemps):

#         if i != 0 and i % print_progress == 0:
#             completed += progress

#             min_now = min(steps)
#             steps.clear()
#             steps.append(min_now)

#             print(f"Walker: {walker} Progress {completed}% Quickest so far: {min_now}")

#         steps.append(try_traversal(False))

#     quickest = min(steps)

#     print("RUN COMPLETE")
#     print("the fastest attemps: ", quickest)

#     result[walker] = quickest

# def find_lowest_steps(attempts, step, use_all_cores=False):

#     if use_all_cores:

#         processes = []

#         cpu_count = multiprocessing.cpu_count() - 1

#         world_result = multiprocessing.Array('i', cpu_count)

#         for i in range(0,cpu_count):

#             child_process = multiprocessing.Process(
#                 target = thread_find_lowest_steps,
#                 args=(i, iterations, step, work_result,),
#             )
#             child_process.start()

#             print(f"Worker {i} started with pid of {child_process.pid}")

#             processes.append(child_process)

#         for process in processes:
#             process.join()

#         print("the shortest traversal...: ", min(work_result))

#     else:
#         thread_find_lowest_steps(0,iterations, step, None)

# # TRAVERSAL TEST
# def test_traversal():
#     visited_rooms = set()
#     traversal_path = try_traversal()
#     player.current_room = world.starting_room
#     visited_rooms.add(player.current_room)

#     for move in traversal_path:
#         player.travel(move)
#         visited_rooms.add(player.current_room)

#     if len(visited_rooms) == len(room_graph):
#         print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
#     else:
#         print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#         print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")