
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top == None
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top 
        # print("Next value :", newNode.next.data)
        self.top = newNode
        # print("top value :", self.top.data)
        self.size += 1
        # print(self.size)

    def traverse(self):
        temp = self.top
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print()

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        print(self.top.data)
        return self.top.data

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        popped_value = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_value

s = Stack()
s.push(1)
# s.traverse()
s.push(2)
s.peek()
# s.traverse()
# s.push(3)
# s.traverse()