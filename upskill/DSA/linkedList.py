class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def pop_first(self):
        if self.head is None:
            return None  # List is empty
        popped = self.head.data
        self.head = self.head.next  # Move head to next node
        return popped

    def pop_last(self):
        if self.head == None:
            return None
        
        if self.head.next == None:
            popped = self.head.data
            self.head = None
            return popped

        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        return current.data
            


    def traverse(self):

        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

    def reverse(self):
        # reverse = '' 
        if self.head:
            popped = 1.1
        while popped:
            print(popped)
            popped = self.pop_last()

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)

# print(l.pop_last())
# l.traverse()
# print(l.pop_last())
# l.traverse()

l.reverse()