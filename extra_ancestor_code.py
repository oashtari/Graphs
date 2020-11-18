# def earliest_ancestor(ancestors, starting_node, path=None, graph=None):
#     graph = {}
#     for (p,c) in ancestors:
#         if c in graph:
#             graph[c].add(p)
#         else:
#             graph[c] = set()
#             graph[c].add(p)

#     result = [-1]
#     print('THE graph', graph)

#     stack = []
#     stack.append([starting_node])
#     visited = set()

#     while len(stack) > 0:
#         path = stack.pop()
#         print('stack path', path)
#         current = path[-1]
#         print('current', current)

#         if current not in visited:
#             visited.add(current)
#             print('visited', visited)

#         if current in graph:
#             for v in graph[current]:
#                 print('the v', v)
#                 new_path = list(path)
#                 new_path.append(v)
#                 stack.append(new_path)
#             print('graph current', current)
#             print('new path', new_path)

#         if len(result) < len(path):
#             result = path
#             print('result', result)
#         elif len(result) == len(path) and result[-1] > current:
#             result = path
#             print('else result', result)

#     return result[-1]