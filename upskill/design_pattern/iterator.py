# 📌 Purpose
# The Iterator Pattern provides a way to access elements of a collection sequentially without exposing its underlying structure.
# It abstracts the logic of iterating over a data structure like list, tree, or custom containers.


# 🎯 Real-Life Analogy
# Imagine a TV remote:

# You don’t care how channels are stored internally.

# You just press next/prev to move through them.

# The remote is the iterator, and the TV is the collection.


from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self): pass

    @abstractmethod
    def next(self): pass



class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self): pass


class Friend:
    def __init__(self, name):
        self.name = name

class FriendCollection(IterableCollection):
    def __init__(self):
        self.friends = []

    def add_friend(self, friend: Friend):
        self.friends.append(friend)

    def create_iterator(self):
        return FriendIterator(self.friends)

class FriendIterator(Iterator):
    def __init__(self, friends):
        self.friends = friends
        self.position = 0

    def has_next(self):
        return self.position < len(self.friends)

    def next(self):
        if self.has_next():
            friend = self.friends[self.position]
            self.position += 1
            return friend
        else:
            raise StopIteration("No more friends.")
if __name__ == "__main__":
    collection = FriendCollection()
    collection.add_friend(Friend("Alice"))
    collection.add_friend(Friend("Bob"))
    collection.add_friend(Friend("Charlie"))
    collection.add_friend(Friend("Diana"))

    iterator = collection.create_iterator()

    print("Iterating over friends:")
    while iterator.has_next():
        friend = iterator.next()
        print(f"Friend: {friend.name}")



# 🔄 Use Cases
# Scenario	Why Iterator Pattern Helps
# Tree traversal	Hide recursion from client
# File system browsing	Next/previous file
# Social media feeds	Scroll through data lazily
# Custom data structures	Provide external iteration
# Database cursor	Fetch rows without exposing logic