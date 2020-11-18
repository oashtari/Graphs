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


