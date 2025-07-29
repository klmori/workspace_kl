# ✅ Purpose
# The Mediator pattern centralizes communication between components (colleagues) so they don’t communicate with each other directly. This reduces tight coupling and makes the system easier to maintain.


# 🏢 Real-Life Analogy: Air Traffic Control (ATC)
# Planes (colleagues) don’t talk to each other directly — instead, they communicate via ATC (mediator), which controls landing, takeoff, and ensures safety.


# 🔧 Use Case Example: Chat Room System
# Users (Colleagues) send messages.

# ChatRoom (Mediator) routes messages to the right recipient.




from abc import ABC, abstractmethod


# -------- Mediator Interface --------
class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, sender, receiver_name, message):
        pass

    @abstractmethod
    def add_user(self, user):
        pass


# -------- Concrete Mediator --------
class ChatRoom(ChatRoomMediator):
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.name] = user
        user.set_mediator(self)

    def show_message(self, sender, receiver_name, message):
        if receiver_name not in self.users:
            print(f"[ChatRoom] User '{receiver_name}' not found.")
            return
        receiver = self.users[receiver_name]
        print(f"[{sender.name} ➡ {receiver.name}]: {message}")
        receiver.receive_message(sender.name, message)


# -------- Colleague Interface --------
class User(ABC):
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    @abstractmethod
    def send(self, receiver_name, message): pass

    @abstractmethod
    def receive_message(self, sender_name, message): pass


# -------- Concrete Colleague --------
class ConcreteUser(User):
    def send(self, receiver_name, message):
        if self.mediator:
            self.mediator.show_message(self, receiver_name, message)

    def receive_message(self, sender_name, message):
        print(f"[{self.name}'s Inbox] From {sender_name}: {message}")


# -------- Client Code --------
if __name__ == "__main__":
    chatroom = ChatRoom()

    alice = ConcreteUser("Alice")
    bob = ConcreteUser("Bob")
    charlie = ConcreteUser("Charlie")

    chatroom.add_user(alice)
    chatroom.add_user(bob)
    chatroom.add_user(charlie)

    alice.send("Bob", "Hi Bob, how are you?")
    bob.send("Alice", "Hey Alice, I’m good!")
    charlie.send("Bob", "Yo Bob, up for a game?")
    alice.send("Dave", "Are you there?")  # Dave not in chatroom
