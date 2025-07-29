class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        val = self.front.data
        self.front = self.front.next
        if self.front is None:  # Queue became empty
            self.rear = None
        return val

    def peek(self):
        return self.front.data if self.front else None

    def is_empty(self):
        return self.front is None
q = LinkedListQueue()
q.enqueue(10)
q.enqueue(20)
print(q.peek())
print(q.dequeue())  # 10
print(q.peek())     # 20




class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.size = capacity
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:  # First element
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None

        val = self.queue[self.front]
        if self.front == self.rear:  # Only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val

    def peek(self):
        if self.front == -1:
            return None
        return self.queue[self.front]

    def is_empty(self):
        return self.front == -1


cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
print(cq.peek())
cq.enqueue(3)  # Full now
cq.dequeue()   # 1 removed
cq.enqueue(4)  # wraps around
print(cq.peek())  # 2
