import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        
        self.friendships[user_id].add(friend_id)
        self.friendships[friend_id].add(user_id)
        return True


    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def get_friends(self, user_id):
        if self.friendships.get(user_id):
            return self.friendships[user_id]
        else:
            return None

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")


        # Create friendships
        """
        possible_friendships = []
        friendship_used = set()

        for user_id in self.users:
            for friend_id in self.users:
                if user_id == friend_id: continue
                if (user_id, friend_id) in friendship_used: continue #to ensure we don't get same friendships twice

                possible_friendships.append((user_id, friend_id))
                friendship_used.add((friend_id, user_id))
        """

        # another solution for above, we're just avoiding even creating a reserver user/friend match with that 2nd line of code

        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))


        random.shuffle(possible_friendships)
        # print(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            # self.add_friendship(*friendship)      #same as above, a shorthand version 


    def populate_graph_2(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.add_user(f"User {i+1}")

        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions +=1 




    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()

            vertex = path[-1]

            if vertex not in visited:
                visited[vertex] = path

                for friend in self.get_friends(vertex):

                    new_path = path.copy()
                    new_path.append(friend)

                    q.enqueue(new_path)


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populate_graph(1000, 2)
    sg.populate_graph_2(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(9)
    print(connections)


# TIM'S SOLUTION

# import random
# from collections import deque
# import time
# ​
# class Queue():
#     def __init__(self):
#         self.queue = deque()
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.popleft()
#         else:
#             return None
#     def size(self):
#         return len(self.queue)
# ​
# ​
# class User:
#     def __init__(self, name):
#         self.name = name
# ​
# class SocialGraph:
#     def __init__(self):
#         self.last_id = 0      # current number of users
#         self.users = {}       # your users with their attributes
#         self.friendships = {} # adjacency list
# ​
#     def add_friendship(self, user_id, friend_id):
#         """
#         Creates a bi-directional friendship
#         """
#         if user_id == friend_id:
#             # print("WARNING: You cannot be friends with yourself")
#             return False
#         elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
#             # print("WARNING: Friendship already exists")
#             return False
#         else:
#             self.friendships[user_id].add(friend_id)
#             self.friendships[friend_id].add(user_id)
#             return True
# ​
#     def add_user(self, name):
#         """
#         Create a new user with a sequential integer ID
#         """
#         self.last_id += 1  # automatically increment the ID to assign the new user
#         self.users[self.last_id] = User(name)
#         self.friendships[self.last_id] = set()
# ​
#     def fisher_yates_shuffle(self, l):
#         for i in range(0, len(l)):
#             random_index = random.randint(i, len(l) - 1)
#             l[random_index], l[i] = l[i], l[random_index]
# ​
#     def populate_graph(self, num_users, avg_friendships):
#         """
#         Takes a number of users and an average number of friendships
#         as arguments
# ​
#         Creates that number of users and a randomly distributed friendships
#         between those users.
# ​
#         The number of users must be greater than the average number of friendships.
#         """
#         # Reset graph
#         self.last_id = 0
#         self.users = {}
#         self.friendships = {}
# ​
#         # Add users
#         for user in range(num_users):
#             self.add_user(user)
# ​
#         # Create friendships
#         # if 1 is a friend of 2, and 2 is a friend of 1, count this as 2 friendships
#         total_friendships = avg_friendships * num_users
        
#         # create a list with all possible friendship combinations, 
#         # friendship_combos = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
#         friendship_combos = []
# ​
#         for user_id in range(1, num_users + 1):
#         # You can avoid this by only creating friendships where user1 < user2
#             for friend_id in range(user_id + 1, num_users + 1):
#                 friendship_combos.append((user_id, friend_id))
# ​
#         # shuffle the list, 
#         self.fisher_yates_shuffle(friendship_combos)
#     # then grab the first N elements from the list
#         friendships_to_make = friendship_combos[:(total_friendships // 2)]
# ​
#         for friendship in friendships_to_make:
#             self.add_friendship(friendship[0], friendship[1])
# ​
#     # so it wouldn't create ALL friendships...just a few random ones somehow. 
# ​
#     # Make two user lists, shuffle one, zip them into a list of the desired number of friendship tuples
#         ## Linear to make the two user lists
#         ## shuffle one: linear
#         ## loop over them both to combine them into random friendship pairs
# ​
#     def populate_graph_linear(self, num_users, avg_friendships):
#         self.last_id = 0
#         self.users = {}
#         self.friendships = {}
# ​
#         # Add users
#         for user in range(num_users):
#             self.add_user(user)
# ​
#         # Create friendships
#         # if 1 is a friend of 2, and 2 is a friend of 1, count this as 2 friendships
#         total_friendships = avg_friendships * num_users
#         friendships_made = 0
        
#         # do this until we have as many as we want
#         while friendships_made < total_friendships:
#     # choose two random user ids
#             first_user = random.randint(1, num_users)
#             second_user = random.randint(1, num_users)
#     # try to make the friendship
#             new_friendship = self.add_friendship(first_user, second_user)
# ​
#             if new_friendship:
#                 friendships_made += 2
# ​
# ​
            
#     def get_friends(self, current_friend):
#         return self.friendships[current_friend]
# ​
# ​
#     def get_all_social_paths(self, user_id):
#         """
#         Takes a user's user_id as an argument
# ​
#         Returns a dictionary containing every user in that user's
#         extended network with the shortest friendship path between them.
# ​
#         The key is the friend's ID and the value is the path.
# ​
#         "wait wait don't tell me" --> "ah ha!"
        
#         Choose your fighter: BFT
# ​
#         """
#         q = Queue()
#         # key: user_id, value: path
#         visited = {}  # Note that this is a dictionary, not a set
# ​
#         q.enqueue([user_id])
# ​
#         while q.size() > 0:
# ​
#             # get the next person in line
#             current_path = q.dequeue()
#             current_person = current_path[-1]
# ​
#             # check if we've visited them yet
#             if current_person not in visited:
#             ## if not, mark as visited
#                 # key: user_id, value: path
#                 visited[current_person] = current_path
#                 ## get their friends (visited their edges)
#                 friends = self.get_friends(current_person)
# ​
#             ## enqueue them
#                 for friend in friends:
#                     friend_path = list(current_path)
#                     # friend_path = [*current_path]
# ​
#                     friend_path.append(friend)
# ​
#                     q.enqueue(friend_path)
# ​
#         return visited
# ​
# ​
# if __name__ == '__main__':
#     sg = SocialGraph()
#     num_users = 1000
#     avg_friendships = 900
# ​
#     start_time = time.time()
#     sg.populate_graph(num_users, avg_friendships)
#     end_time = time.time()
# ​
#     print(end_time - start_time)
# ​
#     start_time = time.time()
#     sg.populate_graph_linear(num_users, avg_friendships)
#     end_time = time.time()
# ​
#     print(end_time - start_time)
# ​
    
#     # print(sg.friendships)
#     # connections = sg.get_all_social_paths(1)
#     # print(connections)
# ​
# # percentage of other users in extended social network
#     # number of people we visited / total number of people
#     # print(len(connections) / num_users)
# ​
# # avg degree of separation --> average steps we took to visit someone
# # just average the length of each path
#     # total_path_lengths = 0
#     # for key, value in connections.items():
#     #     total_path_lengths += len(value)
# ​
#     # average_path_length = total_path_lengths / len(connections)
#     # print(average_path_length)