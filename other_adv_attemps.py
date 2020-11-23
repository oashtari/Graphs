

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